import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { courseApi, Module } from '../services/courses'

export default function CourseList() {
  const [modules, setModules] = useState<Module[]>([])
  const [loading, setLoading] = useState(true)
  const [viewMode, setViewMode] = useState<'cards' | 'timeline'>('cards')
  
  useEffect(() => {
    loadModules()
  }, [])
  
  const loadModules = async () => {
    try {
      const data = await courseApi.getModules()
      setModules(data)
    } catch (error) {
      console.error('Failed to load modules:', error)
    } finally {
      setLoading(false)
    }
  }
  
  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-gray-500 dark:text-gray-400">加载中...</div>
      </div>
    )
  }
  
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          课程列表
        </h1>
        <div className="flex space-x-2">
          <button
            onClick={() => setViewMode('cards')}
            className={`px-3 py-1 rounded ${
              viewMode === 'cards'
                ? 'bg-primary-600 text-white'
                : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300'
            }`}
          >
            卡片
          </button>
          <button
            onClick={() => setViewMode('timeline')}
            className={`px-3 py-1 rounded ${
              viewMode === 'timeline'
                ? 'bg-primary-600 text-white'
                : 'bg-gray-200 dark:bg-gray-700 text-gray-700 dark:text-gray-300'
            }`}
          >
            时间线
          </button>
        </div>
      </div>
      
      {viewMode === 'cards' ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {modules.map((module) => (
            <Link
              key={module.id}
              to={`/courses/${module.id}`}
              className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm hover:shadow-md transition"
            >
              <div className="flex items-center justify-between mb-4">
                <span className="text-sm text-gray-500 dark:text-gray-400">
                  模块 {module.order_index}
                </span>
                <span className="text-sm text-primary-600">
                  {module.completed_count}/{module.lesson_count} 完成
                </span>
              </div>
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
                {module.name}
              </h3>
              <p className="text-sm text-gray-600 dark:text-gray-400 mb-4">
                {module.description}
              </p>
              <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2">
                <div
                  className="bg-primary-600 h-2 rounded-full"
                  style={{
                    width: `${(module.completed_count / module.lesson_count) * 100}%`
                  }}
                />
              </div>
            </Link>
          ))}
        </div>
      ) : (
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <div className="space-y-4">
            {modules.map((module) => (
              <div key={module.id} className="border-l-2 border-primary-500 pl-4">
                <h3 className="font-semibold text-gray-900 dark:text-white">
                  {module.name}
                </h3>
                <p className="text-sm text-gray-600 dark:text-gray-400">
                  {module.completed_count}/{module.lesson_count} 课程完成
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
