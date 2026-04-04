import React from 'react'

interface Article {
  id: string
  title: string
  summary: string | null
  source: string
  source_url: string
  category: string
  published_at: string | null
  view_count: number
}

interface ArticleListProps {
  articles: Article[]
  loading: boolean
  onCategoryChange?: (category: string) => void
  categories: string[]
  selectedCategory: string
  showViewAll?: boolean
}

function formatRelativeTime(dateStr: string | null): string {
  if (!dateStr) return ''
  const date = new Date(dateStr)
  const now = new Date()
  const diffMs = now.getTime() - date.getTime()
  const diffMins = Math.floor(diffMs / 60000)
  const diffHours = Math.floor(diffMins / 60)
  const diffDays = Math.floor(diffHours / 24)

  if (diffMins < 1) return '刚刚'
  if (diffMins < 60) return `${diffMins}分钟前`
  if (diffHours < 24) return `${diffHours}小时前`
  if (diffDays < 7) return `${diffDays}天前`
  return date.toLocaleDateString('zh-CN')
}

function getCategoryColor(category: string): string {
  const colors: Record<string, string> = {
    general: 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300',
    ai: 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-300',
    technology: 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-300',
    education: 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300',
    research: 'bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-300',
  }
  return colors[category] || colors.general
}

export default function ArticleList({
  articles,
  loading,
  onCategoryChange,
  categories,
  selectedCategory,
  showViewAll = true,
}: ArticleListProps) {
  if (loading) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {[1, 2, 3].map((i) => (
          <div key={i} className="bg-white dark:bg-gray-800 rounded-lg shadow-sm p-6 animate-pulse">
            <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-3/4 mb-4"></div>
            <div className="h-3 bg-gray-200 dark:bg-gray-700 rounded w-full mb-2"></div>
            <div className="h-3 bg-gray-200 dark:bg-gray-700 rounded w-2/3"></div>
          </div>
        ))}
      </div>
    )
  }

  if (articles.length === 0) {
    return (
      <div className="text-center py-12 text-gray-500 dark:text-gray-400">
        暂无文章
      </div>
    )
  }

  return (
    <div className="space-y-6">
      {/* 分类筛选 */}
      {onCategoryChange && (
        <div className="flex flex-wrap gap-2">
          <button
            onClick={() => onCategoryChange('')}
            className={`px-3 py-1.5 text-sm font-medium rounded-full transition ${
              selectedCategory === ''
                ? 'bg-primary-600 text-white'
                : 'bg-gray-100 text-gray-700 dark:bg-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'
            }`}
          >
            全部
          </button>
          {categories.map((category) => (
            <button
              key={category}
              onClick={() => onCategoryChange(category)}
              className={`px-3 py-1.5 text-sm font-medium rounded-full transition ${
                selectedCategory === category
                  ? 'bg-primary-600 text-white'
                  : 'bg-gray-100 text-gray-700 dark:bg-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-600'
              }`}
            >
              {category}
            </button>
          ))}
        </div>
      )}

      {/* 文章网格 */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {articles.map((article) => (
          <a
            key={article.id}
            href={article.source_url}
            target="_blank"
            rel="noopener noreferrer"
            className="group bg-white dark:bg-gray-800 rounded-lg shadow-sm hover:shadow-md transition-all duration-200 overflow-hidden border border-gray-100 dark:border-gray-700 hover:-translate-y-1"
          >
            <div className="p-5">
              {/* 分类标签和外链图标 */}
              <div className="flex items-center justify-between mb-3">
                <span
                  className={`inline-block px-2.5 py-1 text-xs font-medium rounded-full ${getCategoryColor(
                    article.category
                  )}`}
                >
                  {article.category}
                </span>
                <svg className="w-4 h-4 text-gray-400 dark:text-gray-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                </svg>
              </div>

              {/* 标题 */}
              <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2 line-clamp-2 group-hover:text-primary-600 dark:group-hover:text-primary-400 transition-colors">
                {article.title}
              </h3>

              {/* 摘要 */}
              {article.summary && (
                <p className="text-sm text-gray-600 dark:text-gray-400 mb-4 line-clamp-3">
                  {article.summary}
                </p>
              )}

              {/* 元信息 */}
              <div className="flex items-center justify-between text-xs text-gray-500 dark:text-gray-400 mt-auto">
                <span>{article.source}</span>
                <div className="flex items-center gap-3">
                  <span>{formatRelativeTime(article.published_at)}</span>
                  {article.view_count > 0 && (
                    <span className="flex items-center gap-1">
                      <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                      </svg>
                      {article.view_count}
                    </span>
                  )}
                </div>
              </div>
            </div>
          </a>
        ))}
      </div>

      {/* 查看全部链接 */}
      {showViewAll && (
        <div className="text-center">
          <a
            href="/articles"
            className="inline-flex items-center text-primary-600 dark:text-primary-400 hover:text-primary-700 dark:hover:text-primary-300 font-medium transition"
          >
            查看全部文章
            <svg className="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </a>
        </div>
      )}
    </div>
  )
}