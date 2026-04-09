import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import logging

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='health_monitor.log'
)

# 配置参数
WEBSITE_URL = "https://www.fphcare.com.cn"
CHECK_INTERVAL = 10  # 分钟

# 邮件配置
EMAIL_CONFIG = {
    "smtp_server": "mail.fphcare.com.cn",
    "smtp_port": 587,
    "sender_email": "no-reply@mail.fphcare.com.cn",
    "sender_password": "your_email_password",
    "receiver_email": "dlinhu@163.com"
}

# 短信配置（需要根据实际情况修改，这里使用阿里云短信服务作为示例）
SMS_CONFIG = {
    "access_key_id": "your_access_key_id",
    "access_key_secret": "your_access_key_secret",
    "sign_name": "your_sign_name",
    "template_code": "your_template_code",
    "phone_numbers": "your_phone_number"
}

def send_email(subject, message):
    """发送邮件通知"""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG["sender_email"]
        msg['To'] = EMAIL_CONFIG["receiver_email"]
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain', 'utf-8'))
        
        server = smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["smtp_port"])
        server.starttls()
        server.login(EMAIL_CONFIG["sender_email"], EMAIL_CONFIG["sender_password"])
        text = msg.as_string()
        server.sendmail(EMAIL_CONFIG["sender_email"], EMAIL_CONFIG["receiver_email"], text)
        server.quit()
        logging.info("邮件发送成功")
    except Exception as e:
        logging.error(f"邮件发送失败: {str(e)}")

def send_sms(message):
    """发送短信通知（示例，需要根据实际短信服务修改）"""
    try:
        # 这里使用阿里云短信服务作为示例，实际使用时需要安装相应的SDK
        # 例如：pip install alibabacloud-dysmsapi20170525
        # 然后实现具体的短信发送逻辑
        logging.info(f"短信发送: {message}")
        # 实际的短信发送代码
    except Exception as e:
        logging.error(f"短信发送失败: {str(e)}")

def check_website_health():
    """检查网站健康度"""
    logging.info(f"开始检查网站健康度: {WEBSITE_URL}")
    
    try:
        response = requests.get(WEBSITE_URL, timeout=30)
        
        if response.status_code == 200:
            logging.info(f"网站访问正常，状态码: {response.status_code}")
            return True
        else:
            error_message = f"网站访问异常，状态码: {response.status_code}"
            logging.error(error_message)
            send_email("网站健康度警告", error_message)
            send_sms(error_message)
            return False
            
    except requests.exceptions.RequestException as e:
        error_message = f"网站访问失败: {str(e)}"
        logging.error(error_message)
        send_email("网站健康度警告", error_message)
        send_sms(error_message)
        return False

def main():
    """主函数"""
    logging.info("网站健康度监控程序启动")
    
    # 立即执行一次检查
    check_website_health()
    
    # 定时执行检查
    schedule.every(CHECK_INTERVAL).minutes.do(check_website_health)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
