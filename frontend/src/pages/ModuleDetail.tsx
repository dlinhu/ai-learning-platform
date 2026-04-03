import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { courseApi, Lesson, Module } from '../services/courses'

export default function ModuleDetail() {
  const { moduleId } = useParams<{ moduleId: string }>()
  const [module, setModule] = useState<Module | null>(null)
  const [lessons, setLessons] = useState<Lesson[]>([])
  const [loading, setLoading] = useState(true)
  
  useEffect(() => {
    if (moduleId) {
      loadModuleData()
    }
  }, [moduleId])
  
  const loadModuleData = async () => {
    try {
      const moduleData = await courseApi.getModule(moduleId!)
      setModule(moduleData)
      
      const lessonsData = await courseApi.getModuleLessons(moduleId!)
      setLessons(lessonsData)
    } catch (error) {
      console.error('Failed to load module:', error)
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
  
  if (!module) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500 dark:text-gray-400">模块未找到</p>
        <Link to="/courses" className="text-primary-600 hover:underline mt-4 inline-block">
          返回课程列表
        </Link>
      </div>
    )
  }
  
  return (
    <div className="space-y-6">
      <div className="flex items-center space-x-4">
        <Link to="/courses" className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300">
          ← 返回课程列表
        </Link>
      </div>
      
      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
        <div className="flex items-center justify-between mb-4">
          <span className="text-sm text-gray-500 dark:text-gray-400">
            模块 {module.order_index}
          </span>
          <span className="text-sm text-primary-600">
            {module.completed_count}/{module.lesson_count} 完成
          </span>
        </div>
        
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
          {module.name}
        </h1>
        
        {module.description && (
          <p className="text-gray-600 dark:text-gray-400">
            {module.description}
          </p>
        )}
        
        <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2 mt-4">
          <div
            className="bg-primary-600 h-2 rounded-full transition-all"
            style={{
              width: `${module.lesson_count > 0 ? (module.completed_count / module.lesson_count) * 100 : 0}%`
            }}
          />
        </div>
      </div>
      
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm overflow-hidden">
        <div className="p-4 border-b border-gray-200 dark:border-gray-700">
          <h2 className="text-lg font-semibold text-gray-900 dark:text-white">
            课程列表 ({lessons.length})
          </h2>
        </div>
        
        <div className="divide-y divide-gray-200 dark:divide-gray-700">
          {lessons.length === 0 ? (
            <div className="p-8 text-center text-gray-500 dark:text-gray-400">
              暂无课程
            </div>
          ) : (
            lessons.map((lesson, index) => (
              <Link
                key={lesson.id}
                to={`/lesson/${lesson.id}`}
                className="block p-4 hover:bg-gray-50 dark:hover:bg-gray-700/50 transition"
              >
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-4">
                    <div className={`w-8 h-8 rounded-full flex items-center justify-center text-sm font-medium ${
                      lesson.progress_status === 'completed'
                        ? 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400'
                        : lesson.progress_status === 'in_progress'
                        ? 'bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400'
                        : 'bg-gray-100 text-gray-700 dark:bg-gray-700 dark:text-gray-300'
                    }`}>
                      {lesson.progress_status === 'completed' ? '✓' : index + 1}
                    </div>
                    <div>
                      <h3 className="font-medium text-gray-900 dark:text-white">
                        {lesson.title}
                      </h3>
                      <div className="flex items-center flex-wrap gap-2 mt-1">
                        <span className="inline-flex items-center px-2 py-0.5 rounded text-sm font-medium bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400">
                          📅 {lesson.date}
                        </span>
                        {lesson.difficulty === 'advanced' && (
                          <span className="px-2 py-0.5 bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400 text-xs rounded">
                            高级
                          </span>
                        )}
                        {lesson.time_estimate > 60 && (
                          <span className="px-2 py-0.5 bg-orange-100 text-orange-700 dark:bg-orange-900/30 dark:text-orange-400 text-xs rounded">
                            {lesson.time_estimate}分钟
                          </span>
                        )}
                        {lesson.materials_count > 0 && (
                          <span className={`px-2 py-0.5 text-xs rounded-full flex items-center gap-1 ${
                            lesson.materials_count >= 2
                              ? 'bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400'
                              : 'bg-gray-100 text-gray-700 dark:bg-gray-700 dark:text-gray-300'
                          }`}>
                            📚 {lesson.materials_count >= 2 && '✨'} {lesson.materials_count}
                          </span>
                        )}
                        {lesson.material_titles && lesson.material_titles.length > 0 && (
                          <div className="flex flex-wrap gap-1 mt-2">
                            {lesson.material_titles.slice(0, 5).map((title, i) => (
                              <span key={i} className={`px-2 py-0.5 text-xs rounded ${
                                lesson.materials_count >= 2
                                  ? 'bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400'
                                  : 'bg-gray-100 text-gray-700 dark:bg-gray-700 dark:text-gray-300'
                              }`}>
                                {title}
                              </span>
                            ))}
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                  <svg className="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                  </svg>
                </div>
              </Link>
            ))
          )}
        </div>
      </div>
    </div>
  )
}
