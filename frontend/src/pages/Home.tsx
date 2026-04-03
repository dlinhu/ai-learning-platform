import { Link } from 'react-router-dom'
import { useAuthStore } from '../stores/authStore'
import NewsList from '../components/NewsList'

export default function Home() {
  const { user } = useAuthStore()
  
  const features = [
    { icon: '📚', title: '51天课程', desc: '从Prompts到PROD，系统化学习AI技术' },
    { icon: '📊', title: '进度追踪', desc: '实时记录学习状态，可视化学习进度' },
    { icon: '💡', title: '知识扩展', desc: '自动提取术语，AI生成名词解释' },
    { icon: '🎯', title: '学习仪表盘', desc: '统计学习数据，追踪连续学习天数' },
  ]
  
  return (
    <div className="space-y-12">
      <section className="text-center py-12">
        <h1 className="text-4xl font-bold text-gray-900 dark:text-white mb-4">
          Context Engineering 综合课程
        </h1>
        <p className="text-xl text-gray-600 dark:text-gray-400 mb-8">
          从零到英雄，系统化学习AI技术
        </p>
        {user ? (
          <Link
            to="/courses"
            className="inline-flex items-center px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition"
          >
            开始学习
          </Link>
        ) : (
          <Link
            to="/login"
            className="inline-flex items-center px-6 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition"
          >
            立即登录
          </Link>
        )}
      </section>
      
      <section className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {features.map((feature, i) => (
          <div
            key={i}
            className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm hover:shadow-md transition"
          >
            <div className="text-3xl mb-3">{feature.icon}</div>
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
              {feature.title}
            </h3>
            <p className="text-gray-600 dark:text-gray-400 text-sm">
              {feature.desc}
            </p>
          </div>
        ))}
      </section>
      
      <section className="bg-white dark:bg-gray-800 rounded-lg p-8 shadow-sm">
        <h2 className="text-2xl font-bold text-gray-900 dark:text-white mb-6">
          课程模块
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {[
            { name: 'Prompts 提示词工程', days: '5天', color: 'bg-blue-500' },
            { name: 'RAG 检索增强生成', days: '7天', color: 'bg-green-500' },
            { name: 'Agent 智能体', days: '18天', color: 'bg-purple-500' },
            { name: 'Multiple Agents', days: '4天', color: 'bg-orange-500' },
            { name: 'PROD 生产落地', days: '10天', color: 'bg-red-500' },
          ].map((module, i) => (
            <div
              key={i}
              className="flex items-center p-4 border border-gray-200 dark:border-gray-700 rounded-lg"
            >
              <div className={`w-3 h-3 rounded-full ${module.color} mr-3`} />
              <div>
                <div className="font-medium text-gray-900 dark:text-white">
                  {module.name}
                </div>
                <div className="text-sm text-gray-500 dark:text-gray-400">
                  {module.days}
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>
      
      <NewsList />
    </div>
  )
}
