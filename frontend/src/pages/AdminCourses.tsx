import { useEffect, useState } from 'react'
import { adminApi } from '../services/admin'
import { courseApi } from '../services/courses'

interface Module {
  id: string
  name: string
  description: string
  order_index: number
  lesson_count: number
}

interface Lesson {
  id: string
  title: string
  date: string
  topics: string[]
  difficulty: string
  time_estimate: number
  summary?: string
}

interface LessonEditModalProps {
  lesson: Lesson | null
  onClose: () => void
  onSave: () => void
}

function LessonEditModal({ lesson, onClose, onSave }: LessonEditModalProps) {
  const [title, setTitle] = useState(lesson?.title || '')
  const [topics, setTopics] = useState(lesson?.topics?.join(', ') || '')
  const [difficulty, setDifficulty] = useState(lesson?.difficulty || 'basic')
  const [timeEstimate, setTimeEstimate] = useState(lesson?.time_estimate || 60)
  const [summary, setSummary] = useState(lesson?.summary || '')
  const [date, setDate] = useState(lesson?.date || '')
  const [loading, setLoading] = useState(false)

  const handleSave = async () => {
    if (!title.trim()) return
    setLoading(true)
    try {
      if (lesson) {
        await adminApi.updateLesson(lesson.id, {
          title,
          topics: topics.split(',').map(t => t.trim()).filter(Boolean),
          difficulty,
          time_estimate: timeEstimate,
          summary,
          date
        })
      }
      onSave()
    } catch (error) {
      console.error('Failed to save lesson:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-lg w-full">
        <div className="p-4 border-b border-gray-200 dark:border-gray-700 flex justify-between items-center">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
            {lesson ? '编辑课程' : '新增课程'}
          </h3>
          <button onClick={onClose} className="text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div className="p-4 space-y-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">课程标题</label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">标签（逗号分隔）</label>
            <input
              type="text"
              value={topics}
              onChange={(e) => setTopics(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              placeholder="Zero-shot, Few-shot, 提示词"
            />
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">难度</label>
              <select
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              >
                <option value="basic">基础</option>
                <option value="intermediate">中级</option>
                <option value="advanced">高级</option>
              </select>
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">时长（分钟）</label>
              <input
                type="number"
                value={timeEstimate}
                onChange={(e) => setTimeEstimate(parseInt(e.target.value) || 60)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              />
            </div>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">日期</label>
            <input
              type="text"
              value={date}
              onChange={(e) => setDate(e.target.value)}
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
              placeholder="3月16日"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">摘要</label>
            <textarea
              value={summary}
              onChange={(e) => setSummary(e.target.value)}
              rows={3}
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            />
          </div>
        </div>
        <div className="p-4 border-t border-gray-200 dark:border-gray-700 flex justify-end gap-2">
          <button
            onClick={onClose}
            className="px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg"
          >
            取消
          </button>
          <button
            onClick={handleSave}
            disabled={loading || !title.trim()}
            className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50"
          >
            {loading ? '保存中...' : '保存'}
          </button>
        </div>
      </div>
    </div>
  )
}

interface UploadModalProps {
  moduleId: string
  onClose: () => void
  onSuccess: () => void
}

function UploadModal({ moduleId, onClose, onSuccess }: UploadModalProps) {
  const [file, setFile] = useState<File | null>(null)
  const [title, setTitle] = useState('')
  const [date, setDate] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState<any>(null)

  const handleUpload = async () => {
    if (!file) return
    setLoading(true)
    try {
      const res = await adminApi.uploadLesson(moduleId, file, title || undefined, date || undefined)
      setResult(res)
    } catch (error) {
      console.error('Upload failed:', error)
      alert('上传失败')
    } finally {
      setLoading(false)
    }
  }

  const handleConfirm = () => {
    onSuccess()
    onClose()
  }

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div className="bg-white dark:bg-gray-800 rounded-lg max-w-lg w-full">
        <div className="p-4 border-b border-gray-200 dark:border-gray-700 flex justify-between items-center">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white">上传课程文档</h3>
          <button onClick={onClose} className="text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        {!result ? (
          <>
            <div className="p-4 space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">选择文件</label>
                <input
                  type="file"
                  accept=".md,.ipynb,.txt"
                  onChange={(e) => setFile(e.target.files?.[0] || null)}
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                />
                <p className="text-xs text-gray-500 mt-1">支持 .md, .ipynb, .txt 格式</p>
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">标题（可选）</label>
                <input
                  type="text"
                  value={title}
                  onChange={(e) => setTitle(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                  placeholder="留空则自动从文档提取"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">日期（可选）</label>
                <input
                  type="text"
                  value={date}
                  onChange={(e) => setDate(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
                  placeholder="3月16日"
                />
              </div>
            </div>
            <div className="p-4 border-t border-gray-200 dark:border-gray-700 flex justify-end gap-2">
              <button onClick={onClose} className="px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg">
                取消
              </button>
              <button
                onClick={handleUpload}
                disabled={loading || !file}
                className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50"
              >
                {loading ? '解析中...' : '上传并解析'}
              </button>
            </div>
          </>
        ) : (
          <>
            <div className="p-4 space-y-3 max-h-96 overflow-y-auto">
              <div className="bg-green-50 dark:bg-green-900/20 p-3 rounded-lg">
                <p className="text-green-700 dark:text-green-400 font-medium">{result.message}</p>
                {result.ai_enabled !== undefined && (
                  <p className="text-xs text-green-600 dark:text-green-500 mt-1">
                    {result.ai_enabled ? '✨ AI智能解析已启用' : '📝 使用基础解析模式'}
                  </p>
                )}
              </div>
              <div>
                <span className="text-sm text-gray-500 dark:text-gray-400">标题：</span>
                <span className="text-gray-900 dark:text-white font-medium">{result.title}</span>
              </div>
              <div>
                <span className="text-sm text-gray-500 dark:text-gray-400">难度：</span>
                <span className="inline-block px-2 py-0.5 text-xs rounded-full bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300">
                  {result.difficulty === 'basic' ? '基础' : result.difficulty === 'intermediate' ? '中级' : '高级'}
                </span>
                <span className="text-sm text-gray-500 dark:text-gray-400 ml-3">预计时长：</span>
                <span className="text-gray-900 dark:text-white">{result.time_estimate}分钟</span>
              </div>
              {result.topics && result.topics.length > 0 && (
                <div>
                  <span className="text-sm text-gray-500 dark:text-gray-400">主题：</span>
                  <div className="flex flex-wrap gap-1 mt-1">
                    {result.topics.map((topic: string, idx: number) => (
                      <span key={idx} className="px-2 py-0.5 text-xs bg-purple-100 dark:bg-purple-900 text-purple-700 dark:text-purple-300 rounded">
                        {topic}
                      </span>
                    ))}
                  </div>
                </div>
              )}
              <div>
                <span className="text-sm text-gray-500 dark:text-gray-400">摘要：</span>
                <p className="text-gray-900 dark:text-white text-sm mt-1 bg-gray-50 dark:bg-gray-700 p-2 rounded">
                  {result.summary?.slice(0, 200)}{result.summary?.length > 200 ? '...' : ''}
                </p>
              </div>
              {result.knowledge_points && result.knowledge_points.length > 0 && (
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm font-medium text-gray-700 dark:text-gray-300">
                      📚 知识点 ({result.knowledge_points.length}个)
                    </span>
                    <span className="text-xs text-gray-500 dark:text-gray-400">
                      共 {result.questions_count || 0} 道练习题
                    </span>
                  </div>
                  <div className="space-y-2">
                    {result.knowledge_points.map((kp: any, idx: number) => (
                      <div key={idx} className="bg-gray-50 dark:bg-gray-700 p-2 rounded text-sm">
                        <div className="flex items-center justify-between">
                          <span className="font-medium text-gray-900 dark:text-white">{kp.title}</span>
                          <div className="flex items-center gap-2">
                            <span className="text-xs text-gray-500 dark:text-gray-400">{kp.category}</span>
                            {kp.questions_count > 0 && (
                              <span className="px-1.5 py-0.5 text-xs bg-blue-100 dark:bg-blue-900 text-blue-700 dark:text-blue-300 rounded">
                                {kp.questions_count}题
                              </span>
                            )}
                          </div>
                        </div>
                        {kp.description && (
                          <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">{kp.description}</p>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
            <div className="p-4 border-t border-gray-200 dark:border-gray-700 flex justify-end gap-2">
              <button onClick={onClose} className="px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg">
                取消
              </button>
              <button onClick={handleConfirm} className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700">
                确认创建
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  )
}

export default function AdminCourses() {
  const [modules, setModules] = useState<Module[]>([])
  const [lessons, setLessons] = useState<{ [moduleId: string]: Lesson[] }>({})
  const [expandedModules, setExpandedModules] = useState<Set<string>>(new Set())
  const [loading, setLoading] = useState(true)
  const [editingLesson, setEditingLesson] = useState<Lesson | null>(null)
  const [uploadingModuleId, setUploadingModuleId] = useState<string | null>(null)
  const [newModuleName, setNewModuleName] = useState('')
  const [showNewModule, setShowNewModule] = useState(false)

  useEffect(() => {
    loadData()
  }, [])

  const loadData = async () => {
    setLoading(true)
    try {
      const modulesData = await adminApi.getModules()
      setModules(modulesData)
      
      const lessonsData: { [key: string]: Lesson[] } = {}
      for (const module of modulesData) {
        const res = await courseApi.getModuleLessons(module.id)
        lessonsData[module.id] = res
      }
      setLessons(lessonsData)
    } catch (error) {
      console.error('Failed to load data:', error)
    } finally {
      setLoading(false)
    }
  }

  const toggleModule = (moduleId: string) => {
    const newExpanded = new Set(expandedModules)
    if (newExpanded.has(moduleId)) {
      newExpanded.delete(moduleId)
    } else {
      newExpanded.add(moduleId)
    }
    setExpandedModules(newExpanded)
  }

  const handleDeleteLesson = async (lessonId: string) => {
    if (!confirm('确定要删除这个课程吗？此操作不可恢复。')) return
    try {
      await adminApi.deleteLesson(lessonId)
      loadData()
    } catch (error) {
      console.error('Failed to delete lesson:', error)
    }
  }

  const handleCreateModule = async () => {
    if (!newModuleName.trim()) return
    try {
      await adminApi.createModule(newModuleName)
      setNewModuleName('')
      setShowNewModule(false)
      loadData()
    } catch (error) {
      console.error('Failed to create module:', error)
    }
  }

  const handleDeleteModule = async (moduleId: string) => {
    if (!confirm('确定要删除这个模块吗？')) return
    try {
      await adminApi.deleteModule(moduleId)
      loadData()
    } catch (error) {
      alert('无法删除：模块下还有课程')
    }
  }

  if (loading) {
    return <div className="p-8 text-center text-gray-500">加载中...</div>
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">课程管理</h1>
        <button
          onClick={() => setShowNewModule(true)}
          className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700"
        >
          + 新增模块
        </button>
      </div>

      {showNewModule && (
        <div className="bg-white dark:bg-gray-800 rounded-lg p-4 shadow-sm">
          <div className="flex gap-2">
            <input
              type="text"
              value={newModuleName}
              onChange={(e) => setNewModuleName(e.target.value)}
              placeholder="模块名称"
              className="flex-1 px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-700 text-gray-900 dark:text-white"
            />
            <button
              onClick={handleCreateModule}
              className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700"
            >
              创建
            </button>
            <button
              onClick={() => { setShowNewModule(false); setNewModuleName('') }}
              className="px-4 py-2 text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700 rounded-lg"
            >
              取消
            </button>
          </div>
        </div>
      )}

      <div className="space-y-4">
        {modules.map((module) => (
          <div key={module.id} className="bg-white dark:bg-gray-800 rounded-lg shadow-sm overflow-hidden">
            <div
              className="p-4 flex items-center justify-between cursor-pointer hover:bg-gray-50 dark:hover:bg-gray-700"
              onClick={() => toggleModule(module.id)}
            >
              <div className="flex items-center gap-3">
                <svg
                  className={`w-5 h-5 text-gray-400 transition-transform ${expandedModules.has(module.id) ? 'rotate-90' : ''}`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                </svg>
                <div>
                  <h3 className="font-semibold text-gray-900 dark:text-white">{module.name}</h3>
                  <p className="text-sm text-gray-500 dark:text-gray-400">{module.lesson_count} 个课程</p>
                </div>
              </div>
              <div className="flex items-center gap-2" onClick={(e) => e.stopPropagation()}>
                <button
                  onClick={() => setUploadingModuleId(module.id)}
                  className="px-3 py-1 text-sm bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400 rounded hover:bg-green-200 dark:hover:bg-green-900/50"
                >
                  上传课程
                </button>
                <button
                  onClick={() => handleDeleteModule(module.id)}
                  className="px-3 py-1 text-sm bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400 rounded hover:bg-red-200 dark:hover:bg-red-900/50"
                >
                  删除模块
                </button>
              </div>
            </div>
            
            {expandedModules.has(module.id) && (
              <div className="border-t border-gray-200 dark:border-gray-700">
                {lessons[module.id]?.map((lesson) => (
                  <div
                    key={lesson.id}
                    className="p-4 border-b border-gray-100 dark:border-gray-700 last:border-b-0 flex items-center justify-between hover:bg-gray-50 dark:hover:bg-gray-700"
                  >
                    <div>
                      <h4 className="font-medium text-gray-900 dark:text-white">{lesson.title}</h4>
                      <div className="flex items-center gap-2 mt-1">
                        <span className="text-sm text-gray-500 dark:text-gray-400">{lesson.date}</span>
                        {lesson.topics?.length > 0 && (
                          <div className="flex gap-1">
                            {lesson.topics.slice(0, 3).map((topic, i) => (
                              <span key={i} className="px-2 py-0.5 text-xs bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400 rounded">
                                {topic}
                              </span>
                            ))}
                          </div>
                        )}
                      </div>
                    </div>
                    <div className="flex gap-2">
                      <button
                        onClick={() => setEditingLesson(lesson)}
                        className="px-3 py-1 text-sm text-primary-600 hover:text-primary-700 dark:text-primary-400"
                      >
                        编辑
                      </button>
                      <button
                        onClick={() => handleDeleteLesson(lesson.id)}
                        className="px-3 py-1 text-sm text-red-600 hover:text-red-700 dark:text-red-400"
                      >
                        删除
                      </button>
                    </div>
                  </div>
                ))}
                {(!lessons[module.id] || lessons[module.id].length === 0) && (
                  <div className="p-4 text-center text-gray-500 dark:text-gray-400">
                    暂无课程，点击"上传课程"添加
                  </div>
                )}
              </div>
            )}
          </div>
        ))}
      </div>

      {editingLesson && (
        <LessonEditModal
          lesson={editingLesson}
          onClose={() => setEditingLesson(null)}
          onSave={() => { setEditingLesson(null); loadData() }}
        />
      )}

      {uploadingModuleId && (
        <UploadModal
          moduleId={uploadingModuleId}
          onClose={() => setUploadingModuleId(null)}
          onSuccess={loadData}
        />
      )}
    </div>
  )
}
