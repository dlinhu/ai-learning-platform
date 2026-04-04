import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuthStore } from '../stores/authStore'
import ArticleList from '../components/ArticleList'
import api from '../services/api'

interface Article {
  id: string
  title: string
  summary: string | null
  source: string
  category: string
  image_url: string | null
  published_at: string | null
  view_count: number
}

export default function Articles() {
  const { user } = useAuthStore()
  const navigate = useNavigate()
  const [articles, setArticles] = useState<Article[]>([])
  const [loading, setLoading] = useState(true)
  const [categories, setCategories] = useState<string[]>([])
  const [selectedCategory, setSelectedCategory] = useState('')
  const [search, setSearch] = useState('')
  const [page, setPage] = useState(1)
  const [perPage] = useState(12)
  const [total, setTotal] = useState(0)

  // 检查用户权限
  useEffect(() => {
    if (!user) {
      navigate('/login')
    }
  }, [user, navigate])

  // 获取文章列表
  const fetchArticles = async () => {
    setLoading(true)
    try {
      const params = new URLSearchParams()
      params.append('page', page.toString())
      params.append('per_page', perPage.toString())
      if (selectedCategory) params.append('category', selectedCategory)
      if (search) params.append('search', search)

      const response = await api.get(`/articles?${params.toString()}`)
      setArticles(response.data)
      setTotal(response.data.length)
    } catch (err) {
      console.error('Error fetching articles:', err)
    } finally {
      setLoading(false)
    }
  }

  // 获取分类列表
  const fetchCategories = async () => {
    try {
      const response = await api.get('/articles/categories/list')
      setCategories(response.data)
    } catch (err) {
      console.error('Error fetching categories:', err)
    }
  }

  useEffect(() => {
    fetchArticles()
    fetchCategories()
  }, [page, selectedCategory])

  // 搜索处理
  const handleSearch = () => {
    setPage(1)
    fetchArticles()
  }

  return (
    <div className="space-y-6">
      {/* 页面标题 */}
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">文章列表</h1>
          <p className="text-gray-600 dark:text-gray-400">浏览优质学习资源</p>
        </div>
      </div>

      {/* 搜索和筛选 */}
      <div className="bg-white dark:bg-gray-800 rounded-lg p-4 shadow-sm">
        <div className="flex flex-col md:flex-row gap-4">
          <div className="flex-1 flex gap-2">
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
              placeholder="搜索文章标题、内容..."
              className="flex-1 px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
            />
            <button
              onClick={handleSearch}
              className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition"
            >
              搜索
            </button>
          </div>
        </div>
      </div>

      {/* 文章列表 */}
      <ArticleList
        articles={articles}
        loading={loading}
        onCategoryChange={setSelectedCategory}
        categories={categories}
        selectedCategory={selectedCategory}
        showViewAll={false}
      />

      {/* 分页 */}
      {!loading && articles.length > 0 && (
        <div className="flex items-center justify-between bg-white dark:bg-gray-800 rounded-lg p-4 shadow-sm">
          <div className="text-sm text-gray-700 dark:text-gray-300">
            共 {total} 条记录
          </div>
          <div className="flex gap-2">
            <button
              onClick={() => setPage(Math.max(1, page - 1))}
              disabled={page === 1}
              className="px-3 py-1 border border-gray-300 dark:border-gray-600 rounded-md text-sm bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-600 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              上一页
            </button>
            <span className="px-3 py-1 text-gray-700 dark:text-gray-300">
              第 {page} 页
            </span>
            <button
              onClick={() => setPage(page + 1)}
              disabled={articles.length < perPage}
              className="px-3 py-1 border border-gray-300 dark:border-gray-600 rounded-md text-sm bg-white dark:bg-gray-700 text-gray-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-600 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              下一页
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
