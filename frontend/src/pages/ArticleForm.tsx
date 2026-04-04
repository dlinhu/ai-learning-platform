import React, { useState, useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { useAuthStore } from '../stores/authStore'
import api from '../services/api'

interface ArticleFormData {
  title: string
  content: string
  source: string
  source_url: string
  category: string
  summary: string
  author: string
  published_at: string
  is_published: boolean
}

export default function ArticleForm() {
  const { user } = useAuthStore()
  const navigate = useNavigate()
  const { id } = useParams<{ id: string }>()
  const isEdit = !!id

  const [formData, setFormData] = useState<ArticleFormData>({
    title: '',
    content: '',
    source: '',
    source_url: '',
    category: 'general',
    summary: '',
    author: '',
    published_at: '',
    is_published: true
  })

  const [urlInput, setUrlInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [fetching, setFetching] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [success, setSuccess] = useState<string | null>(null)
  const [categories] = useState<string[]>(['general', 'ai', 'technology', 'education', 'research'])

  useEffect(() => {
    if (!user || user.role !== 'admin') {
      navigate('/dashboard')
    }
  }, [user, navigate])

  useEffect(() => {
    if (isEdit) {
      fetchArticle()
    }
  }, [isEdit, id])

  const fetchArticle = async () => {
    if (!id) return
    
    setLoading(true)
    try {
      const response = await api.get(`/articles/${id}`)
      const article = response.data
      setFormData({
        title: article.title,
        content: article.content,
        source: article.source,
        source_url: article.source_url,
        category: article.category,
        summary: article.summary || '',
        author: article.author || '',
        published_at: article.published_at ? new Date(article.published_at).toISOString().split('T')[0] : '',
        is_published: article.is_published
      })
      setUrlInput(article.source_url)
    } catch (err) {
      setError('加载文章失败')
      console.error('Error fetching article:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleFetchUrl = async () => {
    if (!urlInput) {
      setError('请输入URL')
      return
    }

    setFetching(true)
    setError(null)

    try {
      const response = await api.post('/articles/fetch-url', { url: urlInput })
      const urlInfo = response.data

      setFormData(prev => ({
        ...prev,
        source_url: urlInput,
        title: urlInfo.title || '',
        summary: urlInfo.summary || '',
        source: urlInfo.source || '',
        content: urlInfo.summary || '' // 使用摘要作为内容
      }))

      if (!urlInfo.success) {
        setError('抓取信息不完整，请手动补充')
      }
    } catch (err: any) {
      setError(err.response?.data?.detail || '抓取URL失败，请手动填写信息')
      console.error('Error fetching URL:', err)
    } finally {
      setFetching(false)
    }
  }

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value, type, checked } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }))
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError(null)
    setSuccess(null)

    try {
      const data = {
        ...formData,
        published_at: formData.published_at ? new Date(formData.published_at).toISOString() : null
      }

      if (isEdit) {
        await api.put(`/articles/${id}`, data)
        setSuccess('文章更新成功')
      } else {
        await api.post('/articles', data)
        setSuccess('文章创建成功')
      }
      
      setTimeout(() => {
        navigate('/admin/articles')
      }, 1000)
    } catch (err: any) {
      setError(err.response?.data?.detail || '保存文章失败')
      console.error('Error saving article:', err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          {isEdit ? '编辑文章' : '创建文章'}
        </h1>
        <p className="text-gray-600 dark:text-gray-400">
          {isEdit ? '修改文章内容' : '添加新的学习资源'}
        </p>
      </div>

      {error && (
        <div className="bg-red-100 dark:bg-red-900 text-red-700 dark:text-red-300 p-4 rounded-lg">
          {error}
        </div>
      )}
      
      {success && (
        <div className="bg-green-100 dark:bg-green-900 text-green-700 dark:text-green-300 p-4 rounded-lg">
          {success}
        </div>
      )}

      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-6">
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* URL输入和抓取 */}
          <div className="bg-blue-50 dark:bg-blue-900/20 rounded-lg p-4 border border-blue-200 dark:border-blue-800">
            <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
              文章链接 <span className="text-red-500">*</span>
            </label>
            <div className="flex gap-2">
              <input
                type="url"
                value={urlInput}
                onChange={(e) => setUrlInput(e.target.value)}
                placeholder="https://example.com/article"
                className="flex-1 px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
              />
              <button
                type="button"
                onClick={handleFetchUrl}
                disabled={fetching}
                className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
              >
                {fetching ? (
                  <>
                    <svg className="animate-spin h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                    </svg>
                    抓取中...
                  </>
                ) : '抓取信息'}
              </button>
            </div>
            <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
              输入外网文章链接，点击"抓取信息"自动获取标题和摘要
            </p>
          </div>

          {/* 基本信息 */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label htmlFor="title" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                标题 <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                id="title"
                name="title"
                value={formData.title}
                onChange={handleInputChange}
                placeholder="文章标题"
                required
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
              />
            </div>

            <div>
              <label htmlFor="source" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                来源 <span className="text-red-500">*</span>
              </label>
              <input
                type="text"
                id="source"
                name="source"
                value={formData.source}
                onChange={handleInputChange}
                placeholder="文章来源"
                required
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
              />
            </div>

            <div>
              <label htmlFor="category" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                分类
              </label>
              <select
                id="category"
                name="category"
                value={formData.category}
                onChange={handleInputChange}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
              >
                {categories.map((category) => (
                  <option key={category} value={category}>
                    {category}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {/* 摘要 */}
          <div>
            <label htmlFor="summary" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              摘要
            </label>
            <textarea
              id="summary"
              name="summary"
              value={formData.summary}
              onChange={handleInputChange}
              placeholder="文章摘要"
              rows={3}
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
            />
          </div>

          {/* 内容 */}
          <div>
            <label htmlFor="content" className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              内容 <span className="text-red-500">*</span>
            </label>
            <textarea
              id="content"
              name="content"
              value={formData.content}
              onChange={handleInputChange}
              placeholder="文章内容或摘要"
              rows={6}
              required
              className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
            />
          </div>

          {/* 发布状态 */}
          <div className="flex items-center">
            <input
              type="checkbox"
              id="is_published"
              name="is_published"
              checked={formData.is_published}
              onChange={handleInputChange}
              className="h-4 w-4 text-primary-600 focus:ring-primary-500 border-gray-300 rounded"
            />
            <label htmlFor="is_published" className="ml-2 block text-sm text-gray-700 dark:text-gray-300">
              立即发布
            </label>
          </div>

          {/* 按钮 */}
          <div className="flex gap-3">
            <button
              type="button"
              onClick={() => navigate('/admin/articles')}
              className="px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-700 transition"
            >
              取消
            </button>
            <button
              type="submit"
              disabled={loading}
              className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              {loading ? (
                <>
                  <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  保存中...
                </>
              ) : isEdit ? '更新文章' : '创建文章'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}