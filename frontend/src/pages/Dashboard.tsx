import { useEffect, useState } from 'react'
import api from '../services/api'

interface Stats {
  total_lessons: number
  completed_lessons: number
  total_time_spent: number
  completion_rate: number
  current_streak: number
  longest_streak: number
  weekly_study_days: number
  weekly_time_spent: number
  estimated_total_time: number
}

interface ModuleProgress {
  module_id: string
  module_name: string
  total: number
  completed: number
  percentage: number
  time_spent: number
  estimated_time: number
  last_study_date: string | null
}

interface CalendarDay {
  date: string
  time_spent: number
  lessons_completed: number
}

interface WeeklyBreakdown {
  day: string
  time: number
}

interface MonthlyTrend {
  week: string
  time: number
}

interface TimeStats {
  total_time_spent: number
  estimated_total_time: number
  efficiency_rate: number
  daily_average: number
  weekly_breakdown: WeeklyBreakdown[]
  monthly_trend: MonthlyTrend[]
}

function formatTime(minutes: number): string {
  if (minutes < 60) {
    return `${minutes}m`
  }
  const hours = Math.floor(minutes / 60)
  const mins = minutes % 60
  return mins > 0 ? `${hours}h ${mins}m` : `${hours}h`
}

function getRelativeTime(dateStr: string | null): string {
  if (!dateStr) return '未学习'
  
  const date = new Date(dateStr)
  const now = new Date()
  const diffDays = Math.floor((now.getTime() - date.getTime()) / (1000 * 60 * 60 * 24))
  
  if (diffDays === 0) return '今天'
  if (diffDays === 1) return '昨天'
  if (diffDays < 7) return `${diffDays}天前`
  if (diffDays < 30) return `${Math.floor(diffDays / 7)}周前`
  return `${Math.floor(diffDays / 30)}月前`
}

function getProgressColor(percentage: number): string {
  if (percentage >= 80) return 'bg-green-500'
  if (percentage >= 50) return 'bg-blue-500'
  if (percentage >= 25) return 'bg-yellow-500'
  return 'bg-gray-400'
}

export default function Dashboard() {
  const [stats, setStats] = useState<Stats | null>(null)
  const [moduleProgress, setModuleProgress] = useState<ModuleProgress[]>([])
  const [calendar, setCalendar] = useState<CalendarDay[]>([])
  const [timeStats, setTimeStats] = useState<TimeStats | null>(null)
  const [loading, setLoading] = useState(true)
  const [refreshing, setRefreshing] = useState(false)
  
  useEffect(() => {
    loadData()
    
    const interval = setInterval(loadData, 300000)
    return () => clearInterval(interval)
  }, [])
  
  const loadData = async (isRefresh = false) => {
    if (isRefresh) {
      setRefreshing(true)
    }
    try {
      const [statsRes, progressRes, calendarRes, timeStatsRes] = await Promise.all([
        api.get<Stats>('/dashboard/stats'),
        api.get<ModuleProgress[]>('/dashboard/modules'),
        api.get<CalendarDay[]>('/dashboard/calendar'),
        api.get<TimeStats>('/dashboard/time-stats')
      ])
      
      setStats(statsRes.data)
      setModuleProgress(progressRes.data)
      setCalendar(calendarRes.data)
      setTimeStats(timeStatsRes.data)
    } catch (error) {
      console.error('Failed to load dashboard:', error)
    } finally {
      setLoading(false)
      setRefreshing(false)
    }
  }
  
  const handleRefresh = () => {
    loadData(true)
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
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          学习仪表盘
        </h1>
        <button
          onClick={handleRefresh}
          disabled={refreshing}
          className="px-4 py-2 text-sm bg-primary-600 text-white rounded-lg hover:bg-primary-700 disabled:opacity-50 transition-colors"
        >
          {refreshing ? '刷新中...' : '刷新数据'}
        </button>
      </div>
      
      {stats && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
            <div className="text-sm text-gray-500 dark:text-gray-400 mb-1">
              完成进度
            </div>
            <div className="text-3xl font-bold text-gray-900 dark:text-white">
              {stats.completion_rate.toFixed(1)}%
            </div>
            <div className="text-sm text-gray-500 dark:text-gray-400">
              {stats.completed_lessons}/{stats.total_lessons} 课程
            </div>
          </div>
          
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
            <div className="text-sm text-gray-500 dark:text-gray-400 mb-1">
              学习时长
            </div>
            <div className="text-3xl font-bold text-gray-900 dark:text-white">
              {formatTime(stats.total_time_spent)}
            </div>
            <div className="text-sm text-gray-500 dark:text-gray-400">
              预估 {formatTime(stats.estimated_total_time)}
            </div>
          </div>
          
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
            <div className="text-sm text-gray-500 dark:text-gray-400 mb-1">
              连续学习
            </div>
            <div className="text-3xl font-bold text-gray-900 dark:text-white">
              {stats.current_streak} 天
            </div>
            <div className="text-sm text-gray-500 dark:text-gray-400">
              最长: {stats.longest_streak} 天
            </div>
          </div>
          
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
            <div className="text-sm text-gray-500 dark:text-gray-400 mb-1">
              本周学习
            </div>
            <div className="text-3xl font-bold text-gray-900 dark:text-white">
              {stats.weekly_study_days} 天
            </div>
            <div className="text-sm text-gray-500 dark:text-gray-400">
              {formatTime(stats.weekly_time_spent)}
            </div>
          </div>
        </div>
      )}
      
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            模块进度
          </h2>
          <div className="space-y-4">
            {moduleProgress.map((module) => (
              <div key={module.module_id} className="space-y-1">
                <div className="flex justify-between text-sm">
                  <span className="text-gray-700 dark:text-gray-300 font-medium">
                    {module.module_name}
                  </span>
                  <span className="text-gray-500 dark:text-gray-400">
                    {module.completed}/{module.total} | {formatTime(module.time_spent)}/{formatTime(module.estimated_time)}
                  </span>
                </div>
                <div className="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2.5">
                  <div
                    className={`h-2.5 rounded-full transition-all ${getProgressColor(module.percentage)}`}
                    style={{ width: `${module.percentage}%` }}
                  />
                </div>
                <div className="text-xs text-gray-400 dark:text-gray-500">
                  最后学习: {getRelativeTime(module.last_study_date)}
                </div>
              </div>
            ))}
          </div>
        </div>
        
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            学习日历
          </h2>
          <div className="grid grid-cols-7 gap-1">
            {['日', '一', '二', '三', '四', '五', '六'].map((day) => (
              <div
                key={day}
                className="text-center text-xs text-gray-500 dark:text-gray-400 py-1"
              >
                {day}
              </div>
            ))}
            {calendar.map((day, i) => (
              <div
                key={i}
                className={`aspect-square rounded-sm flex items-center justify-center text-xs ${
                  day.lessons_completed > 0
                    ? 'bg-green-500 text-white'
                    : day.time_spent > 0
                    ? 'bg-green-200 dark:bg-green-800 text-green-800 dark:text-green-200'
                    : 'bg-gray-100 dark:bg-gray-700 text-gray-400'
                }`}
                title={`${day.date}: ${day.lessons_completed}课完成, ${day.time_spent}分钟`}
              >
                {new Date(day.date).getDate()}
              </div>
            ))}
          </div>
        </div>
      </div>
      
      {timeStats && (
        <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
          <h2 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
            本周学习时长
          </h2>
          <div className="grid grid-cols-7 gap-2">
            {timeStats.weekly_breakdown.map((day) => (
              <div key={day.day} className="text-center">
                <div className="text-xs text-gray-500 dark:text-gray-400 mb-1">
                  {day.day}
                </div>
                <div 
                  className="bg-primary-500 rounded-t transition-all mx-auto"
                  style={{ 
                    width: '24px', 
                    height: `${Math.max(4, Math.min(80, day.time))}px` 
                  }}
                />
                <div className="text-xs text-gray-600 dark:text-gray-300 mt-1">
                  {formatTime(day.time)}
                </div>
              </div>
            ))}
          </div>
          <div className="mt-4 flex justify-between text-sm text-gray-500 dark:text-gray-400">
            <span>日均学习: {formatTime(timeStats.daily_average)}</span>
            <span>学习效率: {timeStats.efficiency_rate.toFixed(1)}%</span>
          </div>
        </div>
      )}
    </div>
  )
}
