import { useEffect, useState } from 'react'
import { adminApi } from '../services/admin'

interface AISettings {
  provider: string
  openai_api_key: string | null
  openai_base_url: string | null
  local_model_url: string | null
  local_model_name: string | null
}

export default function AdminAISettings() {
  const [settings, setSettings] = useState<AISettings>({
    provider: 'none',
    openai_api_key: '',
    openai_base_url: '',
    local_model_url: '',
    local_model_name: ''
  })
  const [loading, setLoading] = useState(true)
  const [saving, setSaving] = useState(false)
  const [testing, setTesting] = useState(false)
  const [testResult, setTestResult] = useState<{ success: boolean; message: string } | null>(null)
  const [showApiKey, setShowApiKey] = useState(false)

  useEffect(() => {
    loadSettings()
  }, [])

  const loadSettings = async () => {
    setLoading(true)
    try {
      const data = await adminApi.getAISettings()
      setSettings({
        provider: data.provider || 'none',
        openai_api_key: data.openai_api_key || '',
        openai_base_url: data.openai_base_url || '',
        local_model_url: data.local_model_url || '',
        local_model_name: data.local_model_name || ''
      })
    } catch (error) {
      console.error('Failed to load AI settings:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleSave = async () => {
    setSaving(true)
    setTestResult(null)
    try {
      await adminApi.updateAISettings({
        provider: settings.provider,
        openai_api_key: settings.openai_api_key || undefined,
        openai_base_url: settings.openai_base_url || undefined,
        local_model_url: settings.local_model_url || undefined,
        local_model_name: settings.local_model_name || undefined
      })
      alert('AI设置已保存')
      loadSettings()
    } catch (error) {
      console.error('Failed to save AI settings:', error)
      alert('保存失败')
    } finally {
      setSaving(false)
    }
  }

  const handleTest = async () => {
    setTesting(true)
    setTestResult(null)
    try {
      const result = await adminApi.testAISettings({
        provider: settings.provider,
        openai_api_key: settings.openai_api_key || undefined,
        openai_base_url: settings.openai_base_url || undefined,
        local_model_url: settings.local_model_url || undefined,
        local_model_name: settings.local_model_name || undefined
      })
      setTestResult(result)
    } catch (error: any) {
      setTestResult({ success: false, message: error.response?.data?.detail || '测试失败' })
    } finally {
      setTesting(false)
    }
  }

  if (loading) {
    return <div className="p-8 text-center text-gray-500">加载中...</div>
  }

  return (
    <div className="max-w-2xl mx-auto space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">AI设置</h1>
        <button
          onClick={handleSave}
          disabled={saving}
          className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50"
        >
          {saving ? '保存中...' : '保存设置'}
        </button>
      </div>

      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-6 space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-3">
            AI提供商
          </label>
          <div className="space-y-2">
            <label className="flex items-center">
              <input
                type="radio"
                name="provider"
                value="none"
                checked={settings.provider === 'none'}
                onChange={(e) => setSettings({ ...settings, provider: e.target.value })}
                className="mr-2"
              />
              <span className="text-gray-900 dark:text-white">禁用AI功能</span>
            </label>
            <label className="flex items-center">
              <input
                type="radio"
                name="provider"
                value="openai"
                checked={settings.provider === 'openai'}
                onChange={(e) => setSettings({ ...settings, provider: e.target.value })}
                className="mr-2"
              />
              <span className="text-gray-900 dark:text-white">OpenAI (云端)</span>
            </label>
            <label className="flex items-center">
              <input
                type="radio"
                name="provider"
                value="local"
                checked={settings.provider === 'local'}
                onChange={(e) => setSettings({ ...settings, provider: e.target.value })}
                className="mr-2"
              />
              <span className="text-gray-900 dark:text-white">本地大模型 (Ollama等)</span>
            </label>
          </div>
        </div>

        {settings.provider === 'openai' && (
          <div className="space-y-4 border-t border-gray-200 dark:border-gray-700 pt-4">
            <h3 className="text-lg font-medium text-gray-900 dark:text-white">OpenAI 设置</h3>
            
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                API Key
              </label>
              <div className="flex gap-2">
                <input
                  type={showApiKey ? 'text' : 'password'}
                  value={settings.openai_api_key || ''}
                  onChange={(e) => setSettings({ ...settings, openai_api_key: e.target.value })}
                  className="flex-1 px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                  placeholder="sk-..."
                />
                <button
                  onClick={() => setShowApiKey(!showApiKey)}
                  className="px-3 py-2 text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg"
                >
                  {showApiKey ? '隐藏' : '显示'}
                </button>
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                API Base URL (可选，用于代理)
              </label>
              <input
                type="text"
                value={settings.openai_base_url || ''}
                onChange={(e) => setSettings({ ...settings, openai_base_url: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="https://api.openai.com/v1"
              />
            </div>
          </div>
        )}

        {settings.provider === 'local' && (
          <div className="space-y-4 border-t border-gray-200 dark:border-gray-700 pt-4">
            <h3 className="text-lg font-medium text-gray-900 dark:text-white">本地模型设置</h3>
            
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                服务地址
              </label>
              <input
                type="text"
                value={settings.local_model_url || ''}
                onChange={(e) => setSettings({ ...settings, local_model_url: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="http://localhost:11434"
              />
              <p className="text-xs text-gray-500 mt-1">
                Ollama默认: http://localhost:11434 | LM Studio: http://localhost:1234
              </p>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                模型名称
              </label>
              <input
                type="text"
                value={settings.local_model_name || ''}
                onChange={(e) => setSettings({ ...settings, local_model_name: e.target.value })}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                placeholder="llama2, qwen2.5, deepseek-r1..."
              />
            </div>
          </div>
        )}

        {settings.provider !== 'none' && (
          <div className="border-t border-gray-200 dark:border-gray-700 pt-4">
            <button
              onClick={handleTest}
              disabled={testing}
              className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50"
            >
              {testing ? '测试中...' : '测试连接'}
            </button>

            {testResult && (
              <div className={`mt-4 p-3 rounded-lg ${
                testResult.success
                  ? 'bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-400'
                  : 'bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-400'
              }`}>
                {testResult.message}
              </div>
            )}
          </div>
        )}
      </div>

      <div className="bg-blue-50 dark:bg-blue-900/20 rounded-lg p-4">
        <h3 className="text-sm font-medium text-blue-800 dark:text-blue-300 mb-2">使用说明</h3>
        <ul className="text-sm text-blue-700 dark:text-blue-400 space-y-1">
          <li>• <strong>OpenAI</strong>: 需要有效的API Key，可配置代理地址</li>
          <li>• <strong>本地模型</strong>: 支持Ollama、LM Studio等兼容OpenAI API的服务</li>
          <li>• 保存设置后，AI功能将在课程解析、知识点提取等功能中生效</li>
          <li>• API Key会被加密存储，前端只显示掩码后的值</li>
        </ul>
      </div>
    </div>
  )
}
