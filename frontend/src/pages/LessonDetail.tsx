import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { courseApi, Lesson, Content, PracticeQuestion, SubmitAnswerResponse, LessonSection } from '../services/courses'
import api from '../services/api'
import { useTimeTracker } from '../hooks/useTimeTracker'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import rehypeHighlight from 'rehype-highlight'
import 'highlight.js/styles/github.css'

export default function LessonDetail() {
  const { id } = useParams<{ id: string }>()
  const [lesson, setLesson] = useState<Lesson | null>(null)
    const [content, setContent] = useState<Content | null>(null)
    const [activeMaterial, setActiveMaterial] = useState(0)
    const [activeTab, setActiveTab] = useState<'content' | 'knowledge' | 'terms' | 'practice'>('content')
    const [expandedKnowledge, setExpandedKnowledge] = useState<string | null>(null)
    const [loading, setLoading] = useState(true)
    const [practiceQuestions, setPracticeQuestions] = useState<Record<string, PracticeQuestion[]>>({})
    const [selectedAnswers, setSelectedAnswers] = useState<Record<string, string>>({})
    const [submittedAnswers, setSubmittedAnswers] = useState<Record<string, SubmitAnswerResponse>>({})
    const [currentQuestionIndices, setCurrentQuestionIndices] = useState<Record<string, number>>({})
    const [lessonStatus, setLessonStatus] = useState<string>('not_started')
    const [completing, setCompleting] = useState(false)
    const [activeSection, setActiveSection] = useState(0)
  
  useTimeTracker({ 
    lessonId: id!,
    onSaveInterval: 60000
  })
  
  useEffect(() => {
    if (id) {
      loadLesson()
      startLesson(id)
    }
  }, [id])
  
  const startLesson = async (lessonId: string) => {
    try {
      const res = await api.post(`/progress/${lessonId}/start`)
      setLessonStatus(res.data.status)
    } catch (error) {
      console.error('Failed to start lesson:', error)
    }
  }
  
  const handleCompleteLesson = async () => {
    if (!id || completing) return
    
    setCompleting(true)
    try {
      await api.post(`/progress/${id}/complete`)
      setLessonStatus('completed')
      alert('恭喜完成本课程学习！')
    } catch (error) {
      console.error('Failed to complete lesson:', error)
      alert('完成课程失败，请重试')
    } finally {
      setCompleting(false)
    }
  }
  
  const loadLesson = async () => {
    try {
      const data = await courseApi.getLesson(id!)
      setLesson(data)
      
      if (data.materials.length > 0) {
        try {
          const contentData = await courseApi.getContent(data.materials[0].path)
          setContent(contentData)
        } catch (e) {
          console.error('Failed to load content:', e)
        }
      }
    } catch (error) {
      console.error('Failed to load lesson:', error)
    } finally {
      setLoading(false)
    }
  }
  
  const handleMaterialChange = async (index: number) => {
    if (!lesson) return
    setActiveMaterial(index)
    
    try {
      const contentData = await courseApi.getContent(lesson.materials[index].path)
      setContent(contentData)
    } catch (error) {
      console.error('Failed to load content:', error)
    }
  }
  
  const loadPracticeQuestions = async (kpId: string) => {
    if (practiceQuestions[kpId]) return
    try {
      const questions = await courseApi.getPracticeQuestions(kpId)
      setPracticeQuestions(prev => ({ ...prev, [kpId]: questions }))
      setCurrentQuestionIndices(prev => ({ ...prev, [kpId]: 0 }))
    } catch (error) {
      console.error('Failed to load practice questions:', error)
    }
  }
  
  const handleSubmitAnswer = async (questionId: string, answer: string) => {
    try {
      const result = await courseApi.submitAnswer({
        question_id: questionId,
        user_answer: answer
      })
      setSubmittedAnswers(prev => ({ ...prev, [questionId]: result }))
    } catch (error) {
      console.error('Failed to submit answer:', error)
    }
  }
  
  const handleNextQuestion = (kpId: string, totalQuestions: number) => {
    const currentIndex = currentQuestionIndices[kpId] || 0
    if (currentIndex < totalQuestions - 1) {
      setCurrentQuestionIndices(prev => ({ ...prev, [kpId]: currentIndex + 1 }))
    }
  }
  
  const handlePrevQuestion = (kpId: string) => {
    const currentIndex = currentQuestionIndices[kpId] || 0
    if (currentIndex > 0) {
      setCurrentQuestionIndices(prev => ({ ...prev, [kpId]: currentIndex - 1 }))
    }
  }
  
  const renderQuestion = (question: PracticeQuestion, _kpId: string) => {
    const submitted = submittedAnswers[question.id]
    const selectedAnswer = selectedAnswers[question.id] || ''
    
    const handleSelectAnswer = (answer: string) => {
      setSelectedAnswers(prev => ({ ...prev, [question.id]: answer }))
    }
    
    return (
      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
        <div className="flex items-center justify-between mb-4">
          <span className={`px-2 py-1 text-xs rounded ${
            question.difficulty === 3
              ? 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400'
              : question.difficulty === 2
              ? 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400'
              : 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400'
          }`}>
            {question.difficulty === 3 ? '困难' : question.difficulty === 2 ? '中等' : '简单'}
          </span>
          <span className="text-xs text-gray-500 dark:text-gray-400">
            {question.question_type === 'single_choice' && '单选题'}
            {question.question_type === 'multiple_choice' && '多选题'}
            {question.question_type === 'true_false' && '判断题'}
            {question.question_type === 'fill_blank' && '填空题'}
            {question.question_type === 'short_answer' && '简答题'}
          </span>
        </div>

        <p className="text-lg font-medium text-gray-900 dark:text-white mb-4">
          {question.question_text}
        </p>

        {question.question_type === 'single_choice' && (
          <div className="space-y-2">
            {question.options.map((option, i) => (
              <button
                key={i}
                onClick={() => !submitted && handleSelectAnswer(option.charAt(0))}
                disabled={!!submitted}
                className={`w-full text-left p-3 rounded-lg border transition-colors ${
                  selectedAnswer === option.charAt(0)
                    ? 'border-primary-500 bg-primary-50 dark:bg-primary-900/20'
                    : submitted && option.charAt(0) === submitted.correct_answer
                    ? 'border-green-500 bg-green-50 dark:bg-green-900/20'
                    : submitted && selectedAnswer === option.charAt(0)
                    ? 'border-red-500 bg-red-50 dark:bg-red-900/20'
                    : 'border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600'
                }`}
              >
                {option}
              </button>
            ))}
          </div>
        )}

        {question.question_type === 'multiple_choice' && (
          <div className="space-y-2">
            {question.options.map((option, i) => {
              const isSelected = selectedAnswer.includes(option.charAt(0))
              return (
                <button
                  key={i}
                  onClick={() => {
                    if (!submitted) {
                      if (isSelected) {
                        handleSelectAnswer(selectedAnswer.replace(option.charAt(0), '').replace(/,/g, ',').replace(/,,/g, ','))
                      } else {
                        handleSelectAnswer(selectedAnswer ? `${selectedAnswer},${option.charAt(0)}` : option.charAt(0))
                      }
                    }
                  }}
                  disabled={!!submitted}
                  className={`w-full text-left p-3 rounded-lg border transition-colors ${
                    isSelected
                      ? 'border-primary-500 bg-primary-50 dark:bg-primary-900/20'
                      : 'border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600'
                  }`}
                >
                  {option}
                </button>
              )
            })}
          </div>
        )}

        {question.question_type === 'true_false' && (
          <div className="space-y-2">
            {['正确', '错误'].map((option) => (
              <button
                key={option}
                onClick={() => !submitted && handleSelectAnswer(option)}
                disabled={!!submitted}
                className={`w-full text-left p-3 rounded-lg border transition-colors ${
                  selectedAnswer === option
                    ? 'border-primary-500 bg-primary-50 dark:bg-primary-900/20'
                    : submitted && option === submitted.correct_answer
                    ? 'border-green-500 bg-green-50 dark:bg-green-900/20'
                    : 'border-gray-200 dark:border-gray-700 hover:border-gray-300 dark:hover:border-gray-600'
                }`}
              >
                {option}
              </button>
            ))}
          </div>
        )}

        {question.question_type === 'fill_blank' && (
          <input
            type="text"
            value={selectedAnswer}
            onChange={(e) => handleSelectAnswer(e.target.value)}
            disabled={!!submitted}
            placeholder="请输入答案"
            className="w-full p-3 rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        )}

        {question.question_type === 'short_answer' && (
          <textarea
            value={selectedAnswer}
            onChange={(e) => handleSelectAnswer(e.target.value)}
            disabled={!!submitted}
            placeholder="请输入你的答案..."
            rows={4}
            className="w-full p-3 rounded-lg border border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 text-gray-900 dark:text-white focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
        )}

        {!submitted ? (
          <button
            onClick={() => handleSubmitAnswer(question.id, selectedAnswer)}
            disabled={!selectedAnswer}
            className="mt-4 w-full py-2 px-4 bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            提交答案
          </button>
        ) : (
          <div className="mt-4">
            <div className={`p-4 rounded-lg ${
              submitted.is_correct
                ? 'bg-green-50 dark:bg-green-900/20 border border-green-200 dark:border-green-800'
                : 'bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800'
            }`}>
              <p className={`font-medium ${
                submitted.is_correct ? 'text-green-700 dark:text-green-400' : 'text-red-700 dark:text-red-400'
              }`}>
                {submitted.is_correct ? '✓ 回答正确！' : '✗ 回答错误'}
              </p>
              <p className="text-sm text-gray-600 dark:text-gray-400 mt-2">
                正确答案: {submitted.correct_answer}
              </p>
              {submitted.explanation && (
                <p className="text-sm text-gray-600 dark:text-gray-400 mt-2">
                  解析: {submitted.explanation}
                </p>
              )}
            </div>
          </div>
        )}
      </div>
    )
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-gray-500 dark:text-gray-400">加载中...</div>
      </div>
    )
  }

  if (!lesson) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500 dark:text-gray-400">课程未找到</p>
        <Link to="/courses" className="text-primary-600 hover:underline mt-4 inline-block">
          返回课程列表
        </Link>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <Link to={`/courses/${lesson.module_id}`} className="text-gray-500 hover:text-gray-700 dark:text-gray-400 dark:hover:text-gray-300">
          ← 返回模块
        </Link>
        
        {lessonStatus === 'completed' ? (
          <span className="px-3 py-1 bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400 text-sm rounded-full">
            ✓ 已完成
          </span>
        ) : (
          <button
            onClick={handleCompleteLesson}
            disabled={completing}
            className="px-4 py-2 bg-primary-600 text-white text-sm rounded-lg hover:bg-primary-700 disabled:opacity-50 transition-colors"
          >
            {completing ? '处理中...' : '完成学习'}
          </button>
        )}
      </div>
      
      <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
        <div className="flex items-center justify-between mb-4">
          <span className="text-sm text-gray-500 dark:text-gray-400">
            {lesson.date}
          </span>
          <span className={`px-2 py-1 rounded text-xs ${
            lesson.difficulty === 'advanced'
              ? 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400'
              : 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400'
          }`}>
            {lesson.difficulty === 'advanced' ? '高级' : '基础'}
          </span>
        </div>
        
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white mb-4">
          {lesson.title}
        </h1>
        
        <div className="flex flex-wrap gap-2 mb-4">
          {lesson.topics.map((topic, i) => (
            <span
              key={i}
              className="px-2 py-1 bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 text-sm rounded"
            >
              {topic}
            </span>
          ))}
        </div>
        
        <div className="flex items-center text-sm text-gray-500 dark:text-gray-400">
          <span>预计时长: {lesson.time_estimate}分钟</span>
        </div>
      </div>
      
      <div className="border-b border-gray-200 dark:border-gray-700">
        <div className="flex space-x-8">
          <button
            onClick={() => setActiveTab('content')}
            className={`py-3 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'content'
                ? 'border-primary-500 text-primary-600 dark:text-primary-400'
                : 'border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300'
            }`}
          >
            课程内容 {lesson.materials_count > 0 && (
              <span className={`ml-1 px-1.5 py-0.5 text-xs rounded-full ${
                lesson.materials_count >= 3
                  ? 'bg-amber-100 text-amber-700 dark:bg-amber-900/30 dark:text-amber-400'
                  : 'bg-purple-100 text-purple-700 dark:bg-purple-900/30 dark:text-purple-400'
              }`}>
                📚 {lesson.materials_count}
              </span>
            )}
          </button>
          <button
            onClick={() => setActiveTab('knowledge')}
            className={`py-3 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'knowledge'
                ? 'border-primary-500 text-primary-600 dark:text-primary-400'
                : 'border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300'
            }`}
          >
            知识点 ({lesson.knowledge_points?.length || 0})
          </button>
          <button
            onClick={() => setActiveTab('practice')}
            className={`py-3 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'practice'
                ? 'border-primary-500 text-primary-600 dark:text-primary-400'
                : 'border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300'
            }`}
          >
            练习
          </button>
          <button
            onClick={() => setActiveTab('terms')}
            className={`py-3 px-1 border-b-2 font-medium text-sm ${
              activeTab === 'terms'
                ? 'border-primary-500 text-primary-600 dark:text-primary-400'
                : 'border-transparent text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300'
            }`}
          >
            名词解释 ({lesson.terms?.length || 0})
          </button>
        </div>
      </div>
      
      {activeTab === 'content' && (
        lesson.materials.length > 0 ? (
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm overflow-hidden">
            <div className="border-b border-gray-200 dark:border-gray-700">
              <div className="flex overflow-x-auto">
                {lesson.materials.map((material, i) => (
                  <button
                    key={i}
                    onClick={() => handleMaterialChange(i)}
                    className={`px-4 py-3 text-sm font-medium whitespace-nowrap ${
                      activeMaterial === i
                        ? 'border-b-2 border-primary-500 text-primary-600 dark:text-primary-400'
                        : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300'
                    }`}
                  >
                    {material.title}
                  </button>
                ))}
              </div>
            </div>
            
            <div className="p-6 prose dark:prose-invert max-w-none">
              {content?.error ? (
                <div className="text-center py-8">
                  <p className="text-red-500 mb-4">{content.error}</p>
                  <p className="text-gray-500 dark:text-gray-400 text-sm">
                    素材路径: {lesson.materials[activeMaterial]?.path}
                  </p>
                </div>
              ) : content?.type === 'markdown' ? (
                <ReactMarkdown
                  remarkPlugins={[remarkGfm]}
                  rehypePlugins={[rehypeHighlight]}
                >
                  {content.raw || ''}
                </ReactMarkdown>
              ) : (
                <div dangerouslySetInnerHTML={{ __html: content?.html || '' }} />
              )}
            </div>
          </div>
        ) : lesson.structured_content?.sections && lesson.structured_content.sections.length > 0 ? (
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm overflow-hidden">
            <div className="border-b border-gray-200 dark:border-gray-700">
              <div className="flex overflow-x-auto">
                {lesson.structured_content.sections.map((section: LessonSection, idx: number) => (
                  <button
                    key={idx}
                    onClick={() => setActiveSection(idx)}
                    className={`px-4 py-3 text-sm font-medium whitespace-nowrap ${
                      activeSection === idx
                        ? 'border-b-2 border-primary-500 text-primary-600 dark:text-primary-400'
                        : 'text-gray-500 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-300'
                    }`}
                  >
                    {section.title}
                  </button>
                ))}
              </div>
            </div>

            <div className="p-6 prose dark:prose-invert max-w-none">
              <ReactMarkdown
                remarkPlugins={[remarkGfm]}
                rehypePlugins={[rehypeHighlight]}
              >
                {lesson.structured_content?.sections?.[activeSection]?.content || ''}
              </ReactMarkdown>
            </div>
          </div>
        ) : (
          <div className="bg-white dark:bg-gray-800 rounded-lg p-8 shadow-sm text-center">
            <p className="text-gray-500 dark:text-gray-400">该课程暂无学习素材</p>
          </div>
        )
      )}
      
      {activeTab === 'knowledge' && (
        <div className="space-y-4">
          {lesson.knowledge_points?.length > 0 ? (
            lesson.knowledge_points.map((kp, index) => (
              <div key={kp.id || index} className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
                <div 
                  className="flex items-start justify-between mb-2 cursor-pointer"
                  onClick={() => setExpandedKnowledge(expandedKnowledge === kp.id ? null : kp.id)}
                >
                  <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
                    {kp.title}
                  </h3>
                  <span className={`px-2 py-1 text-xs rounded ${
                    kp.importance >= 3
                      ? 'bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400'
                      : kp.importance >= 2
                      ? 'bg-yellow-100 text-yellow-700 dark:bg-yellow-900/30 dark:text-yellow-400'
                      : 'bg-green-100 text-green-700 dark:bg-green-900/30 dark:text-green-400'
                  }`}>
                    {kp.importance >= 3 ? '重要' : kp.importance >= 2 ? '中等' : '了解'}
                  </span>
                </div>
                
                <p className="text-gray-600 dark:text-gray-400 mb-3">
                  {kp.description}
                </p>
                
                {expandedKnowledge === kp.id && (
                  <div className="mt-4 space-y-4 border-t border-gray-200 dark:border-gray-700 pt-4">
                    {kp.related_knowledge && kp.related_knowledge.length > 0 && (
                      <div>
                        <h4 className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">相关知识点:</h4>
                        <div className="flex flex-wrap gap-2">
                          {kp.related_knowledge.map((rk, i) => (
                            <span key={i} className="px-2 py-1 bg-purple-50 dark:bg-purple-900/30 text-purple-700 dark:text-purple-300 text-xs rounded">
                              {rk}
                            </span>
                          ))}
                        </div>
                      </div>
                    )}
                    
                    {kp.key_concepts && kp.key_concepts.length > 0 && (
                      <div>
                        <h4 className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">核心概念:</h4>
                        <ul className="list-disc list-inside text-sm text-gray-600 dark:text-gray-400">
                          {kp.key_concepts.map((concept, i) => (
                            <li key={i}>{concept}</li>
                          ))}
                        </ul>
                      </div>
                    )}
                    
                    {kp.examples && kp.examples.length > 0 && (
                      <div>
                        <h4 className="text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">示例:</h4>
                        <div className="space-y-3">
                          {kp.examples.map((example, i) => (
                            <div key={i} className="bg-gray-50 dark:bg-gray-700/50 rounded p-3">
                              <p className="text-sm font-medium text-gray-700 dark:text-gray-300">{example.title}</p>
                              <pre className="text-xs text-gray-600 dark:text-gray-400 mt-1 whitespace-pre-wrap overflow-x-auto">
                                {example.prompt}
                              </pre>
                              <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                                {example.response}
                              </p>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                    
                    {kp.common_mistakes && kp.common_mistakes.length > 0 && (
                      <div>
                        <h4 className="text-sm font-medium text-red-600 dark:text-red-400 mb-2">常见误区:</h4>
                        <ul className="list-disc list-inside text-sm text-red-600 dark:text-red-400">
                          {kp.common_mistakes.map((mistake, i) => (
                            <li key={i}>{mistake}</li>
                          ))}
                        </ul>
                      </div>
                    )}
                    
                    {kp.best_practices && kp.best_practices.length > 0 && (
                      <div>
                        <h4 className="text-sm font-medium text-green-600 dark:text-green-400 mb-2">最佳实践:</h4>
                        <ul className="list-disc list-inside text-sm text-green-600 dark:text-green-400">
                          {kp.best_practices.map((practice, i) => (
                            <li key={i}>{practice}</li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </div>
                )}
              </div>
            ))
          ) : (
            <div className="bg-white dark:bg-gray-800 rounded-lg p-8 shadow-sm text-center">
              <p className="text-gray-500 dark:text-gray-400">暂无知识点总结</p>
            </div>
          )}
        </div>
      )}
      
      {activeTab === 'practice' && (
        <div className="space-y-6">
          {lesson.knowledge_points?.length > 0 ? (
            lesson.knowledge_points.map((kp) => {
              const questions = practiceQuestions[kp.id] || []
              const hasQuestions = questions && questions.length > 0
              const currentIndex = currentQuestionIndices[kp.id] || 0

              return (
                <div key={kp.id} className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
                  <div className="flex items-center justify-between mb-4">
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
                      {kp.title}
                    </h3>
                    {!hasQuestions && (
                      <button
                        onClick={() => loadPracticeQuestions(kp.id)}
                        className="px-4 py-2 bg-primary-600 text-white text-sm rounded-lg hover:bg-primary-700 transition-colors"
                      >
                        开始练习
                      </button>
                    )}
                  </div>

                  {hasQuestions && (
                    <>
                      <div className="flex items-center justify-between mb-4 text-sm text-gray-500 dark:text-gray-400">
                        <span>题目 {currentIndex + 1} / {questions.length}</span>
                        <div className="flex gap-2">
                          <button
                            onClick={() => handlePrevQuestion(kp.id)}
                            disabled={currentIndex === 0}
                            className="px-3 py-1 border border-gray-300 dark:border-gray-600 rounded hover:bg-gray-50 dark:hover:bg-gray-700 disabled:opacity-50 disabled:cursor-not-allowed"
                          >
                            上一题
                          </button>
                          <button
                            onClick={() => handleNextQuestion(kp.id, questions.length)}
                            disabled={currentIndex === questions.length - 1}
                            className="px-3 py-1 border border-gray-300 dark:border-gray-600 rounded hover:bg-gray-50 dark:hover:bg-gray-700 disabled:opacity-50 disabled:cursor-not-allowed"
                          >
                            下一题
                          </button>
                        </div>
                      </div>

                      <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2 mb-4">
                        <div
                          className="bg-primary-600 h-2 rounded-full transition-all"
                          style={{ width: `${((currentIndex + 1) / questions.length) * 100}%` }}
                        />
                      </div>

                      {renderQuestion(questions[currentIndex], kp.id)}
                    </>
                  )}
                </div>
              )
            })
          ) : (
            <div className="bg-white dark:bg-gray-800 rounded-lg p-8 shadow-sm text-center">
              <p className="text-gray-500 dark:text-gray-400">暂无练习题</p>
            </div>
          )}
        </div>
      )}

      {activeTab === 'terms' && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {lesson.terms?.length > 0 ? (
            lesson.terms.map((term, index) => (
              <div key={term.id || index} className="bg-white dark:bg-gray-800 rounded-lg p-4 shadow-sm">
                <div className="flex items-center justify-between mb-2">
                  <h4 className="font-semibold text-primary-600 dark:text-primary-400">
                    {term.term}
                  </h4>
                  <span className="text-xs text-gray-500 dark:text-gray-400 bg-gray-100 dark:bg-gray-700 px-2 py-1 rounded">
                    {term.category}
                  </span>
                </div>
                <p className="text-sm text-gray-600 dark:text-gray-400 mb-2">
                  {term.definition}
                </p>
                {term.detailed_definition && (
                  <p className="text-xs text-gray-500 dark:text-gray-400 mt-2">
                    {term.detailed_definition}
                  </p>
                )}
                {term.examples && term.examples.length > 0 && (
                  <div className="mt-2">
                    <p className="text-xs font-medium text-gray-500 dark:text-gray-400">示例:</p>
                    <ul className="text-xs text-gray-600 dark:text-gray-400 list-disc list-inside">
                      {term.examples.map((ex, i) => (
                        <li key={i}>{ex}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            ))
          ) : (
            <div className="col-span-2 bg-white dark:bg-gray-800 rounded-lg p-8 shadow-sm text-center">
              <p className="text-gray-500 dark:text-gray-400">暂无名词解释</p>
            </div>
          )}
        </div>
      )}
      
      <div className="flex justify-center pt-4 pb-8">
        {lessonStatus === 'completed' ? (
          <div className="text-center">
            <span className="text-green-600 dark:text-green-400 text-lg">✓ 已完成本课程学习</span>
            <p className="text-sm text-gray-500 dark:text-gray-400 mt-2">
              继续学习其他课程提升自己吧！
            </p>
          </div>
        ) : (
          <button
            onClick={handleCompleteLesson}
            disabled={completing}
            className="px-8 py-3 bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50 transition-colors text-lg"
          >
            {completing ? '处理中...' : '完成本课程学习'}
          </button>
        )}
      </div>
    </div>
  )
}
