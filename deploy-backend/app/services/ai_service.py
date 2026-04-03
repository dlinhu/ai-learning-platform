from abc import ABC, abstractmethod
from typing import Optional
import requests

class AIProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        pass
    
    @abstractmethod
    def test_connection(self) -> tuple[bool, str]:
        pass

class NoneProvider(AIProvider):
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        return "AI功能未配置"
    
    def test_connection(self) -> tuple[bool, str]:
        return True, "AI功能已禁用"

class OpenAIProvider(AIProvider):
    def __init__(self, api_key: str, base_url: Optional[str] = None):
        self.api_key = api_key
        self.base_url = base_url or "https://api.openai.com/v1"
    
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key, base_url=self.base_url)
            
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"OpenAI调用失败: {str(e)}"
    
    def test_connection(self) -> tuple[bool, str]:
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key, base_url=self.base_url)
            client.models.list()
            return True, "OpenAI连接成功"
        except Exception as e:
            return False, f"OpenAI连接失败: {str(e)}"

class LocalModelProvider(AIProvider):
    def __init__(self, url: str, model_name: str):
        self.url = url.rstrip('/')
        self.model_name = model_name
    
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        try:
            if "ollama" in self.url.lower() or ":11434" in self.url:
                return self._call_ollama(prompt, system_prompt)
            else:
                return self._call_openai_compatible(prompt, system_prompt)
        except Exception as e:
            return f"本地模型调用失败: {str(e)}"
    
    def _call_ollama(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        response = requests.post(
            f"{self.url}/api/generate",
            json={
                "model": self.model_name,
                "prompt": prompt,
                "system": system_prompt,
                "stream": False
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json().get("response", "")
    
    def _call_openai_compatible(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = requests.post(
            f"{self.url}/v1/chat/completions",
            json={
                "model": self.model_name,
                "messages": messages,
                "max_tokens": 2000
            },
            timeout=60
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    
    def test_connection(self) -> tuple[bool, str]:
        try:
            if "ollama" in self.url.lower() or ":11434" in self.url:
                response = requests.get(f"{self.url}/api/tags", timeout=5)
                if response.status_code == 200:
                    models = response.json().get("models", [])
                    model_names = [m.get("name", "") for m in models]
                    if self.model_name in model_names or any(self.model_name in n for n in model_names):
                        return True, f"Ollama连接成功，模型 {self.model_name} 可用"
                    else:
                        return False, f"模型 {self.model_name} 不存在，可用模型: {', '.join(model_names)}"
                return False, "Ollama连接失败"
            else:
                response = requests.get(f"{self.url}/v1/models", timeout=5)
                if response.status_code == 200:
                    return True, f"本地模型连接成功"
                return False, "本地模型连接失败"
        except Exception as e:
            return False, f"本地模型连接失败: {str(e)}"

def get_ai_provider(settings) -> AIProvider:
    if not settings or settings.provider == "none":
        return NoneProvider()
    
    if settings.provider == "openai":
        if settings.openai_api_key:
            return OpenAIProvider(settings.openai_api_key, settings.openai_base_url)
        return NoneProvider()
    
    if settings.provider == "local":
        if settings.local_model_url and settings.local_model_name:
            return LocalModelProvider(settings.local_model_url, settings.local_model_name)
        return NoneProvider()
    
    return NoneProvider()
