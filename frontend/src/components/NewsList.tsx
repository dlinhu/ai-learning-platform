import { useEffect, useState } from 'react'
import api from '../services/api'

interface NewsItem {
  id: string
  title: string
  summary: string | null
  source: string
  source_url: string
  category: string
  image_url: string | null
  published_at: string | null
  view_count: number
  is_featured: boolean
}

interface NewsListResponse {
  news: NewsItem[]
  total: number
  page: number
  per_page: number
}

function NewsCard({ news }: { news: NewsItem }) {
  const formatDate = (dateStr: string | null): string => {
    if (!dateStr) return ''
    const date = new Date(dateStr)
    const now = new Date()
    const diffMs = now.getTime() - date.getTime()
    const diffHours = Math.floor(diffMs / (1000 * 60 * 60))
    const diffDays = Math.floor(diffHours / 24)
    
    if (diffHours < 1) return '刚刚'
    if (diffHours < 24) return `${diffHours}小时前`
    if (diffDays < 7) return `${diffDays}天前`
    return date.toLocaleDateString('zh-CN')
  }

  const getCategoryColor = (category: string): string => {
    const colors: Record<string, string> = {
      'OpenAI': 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200',
      'Anthropic': 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200',
      'Google AI': 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-200',
      'AI Industry': 'bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200',
    }
    return colors[category] || 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-200'
  }

  return (
    <a
      href={news.source_url}
      target="_blank"
      rel="noopener noreferrer"
      className="block bg-white dark:bg-gray-800 rounded-lg shadow hover:shadow-md transition-shadow p-4 border border-gray-200 dark:border-gray-700"
    >
      <div className="flex items-start justify-between mb-2">
        <span className={`px-2 py-1 text-xs rounded-full ${getCategoryColor(news.category)}`}>
          {news.category}
        </span>
        <span className="text-xs text-gray-500 dark:text-gray-400">
          {formatDate(news.published_at)}
        </span>
      </div>
      
      <h3 className="text-sm font-semibold text-gray-900 dark:text-white mb-2 line-clamp-2">
        {news.title}
      </h3>
      
      {news.summary && (
        <p className="text-xs text-gray-600 dark:text-gray-400 line-clamp-2 mb-2">
          {news.summary}
        </p>
      )}
      
      <div className="flex items-center justify-between text-xs text-gray-500 dark:text-gray-400">
        <span>{news.source}</span>
        <span>{news.view_count} 阅读</span>
      </div>
    </a>
  )
}

export default function NewsList() {
  const [newsList, setNewsList] = useState<NewsItem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    fetchNews()
  }, [])

  const fetchNews = async () => {
    try {
      setLoading(true)
      const response = await api.get<NewsListResponse>('/news', {
        params: {
          page: 1,
          per_page: 5
        }
      })
      setNewsList(response.data.news)
    } catch (err: any) {
      console.error('Failed to fetch news:', err)
      setError('加载新闻失败')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
          AI 新闻动态
        </h2>
        <div className="text-center py-8 text-gray-500 dark:text-gray-400">
          加载中...
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
          AI 新闻动态
        </h2>
        <div className="text-center py-8 text-red-500">
          {error}
        </div>
      </div>
    )
  }

  if (newsList.length === 0) {
    return (
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
        <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
          AI 新闻动态
        </h2>
        <div className="text-center py-8 text-gray-500 dark:text-gray-400">
          暂无新闻
        </div>
      </div>
    )
  }

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
      <div className="flex items-center justify-between mb-4">
        <h2 className="text-lg font-semibold text-gray-900 dark:text-white">
          AI 新闻动态
        </h2>
        <a
          href="/news"
          className="text-sm text-primary-600 hover:text-primary-700 dark:text-primary-400 dark:hover:text-primary-300"
        >
          查看更多 →
        </a>
      </div>
      
      <div className="space-y-3">
        {newsList.map((news) => (
          <NewsCard key={news.id} news={news} />
        ))}
      </div>
    </div>
  )
}
