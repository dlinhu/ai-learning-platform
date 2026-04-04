import { useEffect, useState } from 'react'
import { useAuthStore } from '../stores/authStore'
import { adminApi, AdminStats, UserListItem, UserDetailResponse, UsersListParams } from '../services/admin'
import GroupProgressModal from './GroupProgressModal'

function formatTime(minutes: number): string {
  if (minutes < 60) {
    return `${minutes}分钟`
  }
  const hours = Math.floor(minutes / 60)
  const mins = minutes % 60
  return mins > 0 ? `${hours}小时${mins}分钟` : `${hours}小时`
}

function formatDate(dateStr: string | null): string {
  if (!dateStr) return '从未活跃'
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

function getProgressColor(percentage: number): string {
  if (percentage >= 80) return 'bg-green-500'
  if (percentage >= 50) return 'bg-blue-500'
  if (percentage >= 25) return 'bg-yellow-500'
  return 'bg-gray-400'
}

export default function AdminDashboard() {
  const { user: currentUser } = useAuthStore()
  const [stats, setStats] = useState<AdminStats | null>(null)
  const [users, setUsers] = useState<UserListItem[]>([])
  const [totalUsers, setTotalUsers] = useState(0)
  const [page, setPage] = useState(1)
  const [totalPages, setTotalPages] = useState(1)
  const [loading, setLoading] = useState(true)
  const [searchTerm, setSearchTerm] = useState('')
  const [sortBy, setSortBy] = useState<UsersListParams['sort_by']>('time_spent')
  const [order, setOrder] = useState<UsersListParams['order']>('desc')
  const [selectedUser, setSelectedUser] = useState<UserDetailResponse | null>(null)
  const [modalLoading, setModalLoading] = useState(false)
  const [showGroupProgress, setShowGroupProgress] = useState(false)
  const [updatingRole, setUpdatingRole] = useState<string | null>(null)
  
  useEffect(() => {
    loadStats()
    loadUsers()
  }, [])
  
  useEffect(() => {
    loadUsers()
  }, [page, sortBy, order])
  
  const loadStats = async () => {
    try {
      const data = await adminApi.getStats()
      setStats(data)
    } catch (error) {
      console.error('Failed to load stats:', error)
    }
  }
  
  const loadUsers = async () => {
    setLoading(true)
    try {
      const data = await adminApi.getUsers({
        page,
        per_page: 10,
        sort_by: sortBy,
        order,
        search: searchTerm || undefined
      })
      setUsers(data.users)
      setTotalUsers(data.total)
      setTotalPages(data.total_pages)
    } catch (error) {
      console.error('Failed to load users:', error)
    } finally {
      setLoading(false)
    }
  }
  
  const handleSearch = () => {
    setPage(1)
    loadUsers()
  }
  
  const handleUserClick = async (userId: string) => {
    setModalLoading(true)
    try {
      const detail = await adminApi.getUserDetail(userId)
      setSelectedUser(detail)
    } catch (error) {
      console.error('Failed to load user detail:', error)
    } finally {
      setModalLoading(false)
    }
  }
  
  const closeModal = () => {
    setSelectedUser(null)
  }
  
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">
          {currentUser?.role === 'group_admin' ? '组长仪表盘' : '管理员仪表盘'}
        </h1>
        <div className="flex items-center gap-2">
          <button
            onClick={() => { loadStats(); loadUsers(); }}
            className="px-4 py-2 text-sm bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
          >
            刷新数据
          </button>
          <button
            onClick={() => setShowGroupProgress(true)}
            className="px-4 py-2 text-sm bg-purple-600 text-white rounded-lg hover:bg-purple-700 transition-colors"
          >
            查看分组进度
          </button>
        </div>
      </div>
      
      {stats && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
            <div className="text-sm text-gray-500 dark:text-gray-400 mb-1">
              总用户数
            </div>
            <div className="text-3xl font-bold text-gray-900 dark:text-white">
              {stats.total_users}
            </div>
          </div>
          
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
            <div className="text-sm text-gray-500 dark:text-gray-400 mb-1">
              今日活跃
            </div>
            <div className="text-3xl font-bold text-green-600 dark:text-green-400">
              {stats.active_users_today}
            </div>
            <div className="text-sm text-gray-500 dark:text-gray-400">
              本周: {stats.active_users_week}
            </div>
          </div>
          
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
            <div className="text-sm text-gray-500 dark:text-gray-400 mb-1">
              总学习时长
            </div>
            <div className="text-3xl font-bold text-blue-600 dark:text-blue-400">
              {formatTime(stats.total_time_spent)}
            </div>
            <div className="text-sm text-gray-500 dark:text-gray-400">
              人均: {formatTime(Math.round(stats.avg_time_per_user))}
            </div>
          </div>
          
          <div className="bg-white dark:bg-gray-800 rounded-lg p-6 shadow-sm">
            <div className="text-sm text-gray-500 dark:text-gray-400 mb-1">
              平均完成率
            </div>
            <div className="text-3xl font-bold text-purple-600 dark:text-purple-400">
              {stats.avg_completion_rate.toFixed(1)}%
            </div>
            <div className="text-sm text-gray-500 dark:text-gray-400">
              总完成: {stats.total_completions}课
            </div>
          </div>
        </div>
      )}
      
      <div className="bg-white dark:bg-gray-800 rounded-lg shadow-sm">
        <div className="p-4 border-b border-gray-200 dark:border-gray-700">
          <div className="flex flex-col sm:flex-row gap-4">
            <div className="flex-1 flex gap-2">
              <input
                type="text"
                placeholder="搜索用户名或邮箱..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
                className="flex-1 px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
              />
              <button
                onClick={handleSearch}
                className="px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors"
              >
                搜索
              </button>
            </div>
            
            <div className="flex gap-2">
              <select
                value={sortBy}
                onChange={(e) => setSortBy(e.target.value as UsersListParams['sort_by'])}
                className="px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white"
              >
                <option value="time_spent">学习时长</option>
                <option value="completion_rate">完成率</option>
                <option value="last_active">最近活跃</option>
                <option value="username">用户名</option>
              </select>
              
              <select
                value={order}
                onChange={(e) => setOrder(e.target.value as UsersListParams['order'])}
                className="px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-lg dark:bg-gray-700 dark:text-white"
              >
                <option value="desc">降序</option>
                <option value="asc">升序</option>
              </select>
            </div>
          </div>
        </div>
        
        {loading ? (
          <div className="p-8 text-center text-gray-500 dark:text-gray-400">
            加载中...
          </div>
        ) : (
          <>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-gray-50 dark:bg-gray-700">
                  <tr>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                      用户
                    </th>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                      分组
                    </th>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                      学习时长
                    </th>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                      完成课程
                    </th>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                      完成率
                    </th>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                      连续学习
                    </th>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                      最后活跃
                    </th>
                    <th className="px-4 py-3 text-left text-xs font-medium text-gray-500 dark:text-gray-300 uppercase tracking-wider">
                      操作
                    </th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-gray-200 dark:divide-gray-700">
                  {users.map((user) => (
                    <tr key={user.user_id} className="hover:bg-gray-50 dark:hover:bg-gray-700">
                      <td className="px-4 py-4 whitespace-nowrap">
                        <div>
                          <div className="text-sm font-medium text-gray-900 dark:text-white">
                            {user.username}
                          </div>
                          <div className="text-sm text-gray-500 dark:text-gray-400">
                            {user.email}
                          </div>
                        </div>
                      </td>
                      <td className="px-4 py-4 whitespace-nowrap">
                        <div className="flex gap-2">
                          {currentUser?.role === 'admin' && (
                          <select
                            value={user.group || 'group1'}
                            onChange={(e) => {
                              const newGroup = e.target.value
                              adminApi.updateUserGroup(user.user_id, newGroup)
                              setUsers(users.map(u =>
                                u.user_id === user.user_id
                                  ? { ...u, group: newGroup }
                                  : u
                              ))
                            }}
                            className="px-2 py-1 text-xs rounded border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white focus:ring-2 focus:ring-primary-500"
                          >
                            <option value="group1">Group 1</option>
                            <option value="group2">Group 2</option>
                            <option value="group3">Group 3</option>
                            <option value="group4">Group 4</option>
                            <option value="group5">Group 5</option>
                            <option value="group6">Group 6</option>
                          </select>
                          )}
                          <select
                            value={user.role || 'student'}
                            onChange={(e) => {
                              const newRole = e.target.value
                              const roleNames: Record<string, string> = {
                                'student': '学生',
                                'group_admin': '组长',
                                'admin': '管理员'
                              }
                              if (confirm(`确定要将用户 ${user.username} 的角色修改为 ${roleNames[newRole] || newRole} 吗？`)) {
                                adminApi.updateUserRole(user.user_id, newRole)
                                setUsers(users.map(u =>
                                  u.user_id === user.user_id
                                    ? { ...u, role: newRole }
                                    : u
                                ))
                              }
                            }}
                            className={`px-2 py-1 text-xs rounded border ${
                              user.role === 'admin' 
                                ? 'border-purple-500 bg-purple-50 dark:bg-purple-900/20 text-purple-700 dark:text-purple-300' 
                                : user.role === 'group_admin'
                                ? 'border-blue-500 bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-300'
                                : 'border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700 text-gray-900 dark:text-white'
                            } focus:ring-2 focus:ring-primary-500`}
                          >
                            <option value="student">学生</option>
                            {currentUser?.role === 'admin' && (
                              <option value="group_admin">组长</option>
                            )}
                            {currentUser?.role === 'admin' && (
                              <option value="admin">管理员</option>
                            )}
                          </select>
                        </div>
                      </td>
                      <td className="px-4 py-4 whitespace-nowrap text-sm text-gray-900 dark:text-white">
                        {formatTime(user.total_time_spent)}
                      </td>
                      <td className="px-4 py-4 whitespace-nowrap text-sm text-gray-900 dark:text-white">
                        {user.completed_lessons}
                        {user.in_progress_lessons > 0 && (
                          <span className="text-gray-500 dark:text-gray-400 ml-1">
                            (+{user.in_progress_lessons}进行中)
                          </span>
                        )}
                      </td>
                      <td className="px-4 py-4 whitespace-nowrap">
                        <div className="flex items-center">
                          <div className="w-16 bg-gray-200 dark:bg-gray-600 rounded-full h-2 mr-2">
                            <div
                              className={`h-2 rounded-full ${getProgressColor(user.completion_rate)}`}
                              style={{ width: `${Math.min(100, user.completion_rate)}%` }}
                            />
                          </div>
                          <span className="text-sm text-gray-900 dark:text-white">
                            {user.completion_rate.toFixed(1)}%
                          </span>
                        </div>
                      </td>
                      <td className="px-4 py-4 whitespace-nowrap text-sm text-gray-900 dark:text-white">
                        {user.current_streak}天
                      </td>
                      <td className="px-4 py-4 whitespace-nowrap text-sm text-gray-500 dark:text-gray-400">
                        {formatDate(user.last_active)}
                      </td>
                      <td className="px-4 py-4 whitespace-nowrap text-sm">
                        <button
                          onClick={() => handleUserClick(user.user_id)}
                          className="text-primary-600 hover:text-primary-700 dark:text-primary-400 dark:hover:text-primary-300"
                        >
                          查看详情
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            
            {totalPages > 1 && (
              <div className="px-4 py-3 border-t border-gray-200 dark:border-gray-700 flex items-center justify-between">
                <div className="text-sm text-gray-500 dark:text-gray-400">
                  共 {totalUsers} 个用户
                </div>
                <div className="flex gap-2">
                  <button
                    onClick={() => setPage(p => Math.max(1, p - 1))}
                    disabled={page === 1}
                    className="px-3 py-1 border border-gray-300 dark:border-gray-600 rounded-md disabled:opacity-50 dark:bg-gray-700 dark:text-white"
                  >
                    上一页
                  </button>
                  <span className="px-3 py-1 text-gray-700 dark:text-gray-300">
                    {page} / {totalPages}
                  </span>
                  <button
                    onClick={() => setPage(p => Math.min(totalPages, p + 1))}
                    disabled={page === totalPages}
                    className="px-3 py-1 border border-gray-300 dark:border-gray-600 rounded-md disabled:opacity-50 dark:bg-gray-700 dark:text-white"
                  >
                    下一页
                  </button>
                </div>
              </div>
            )}
          </>
        )}
      </div>
      
      {selectedUser && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white dark:bg-gray-800 rounded-lg max-w-4xl w-full max-h-[90vh] overflow-y-auto">
            <div className="p-6 border-b border-gray-200 dark:border-gray-700 flex justify-between items-start">
              <div>
                <h2 className="text-xl font-bold text-gray-900 dark:text-white">
                  用户详情
                </h2>
                <p className="text-gray-500 dark:text-gray-400">
                  {selectedUser.username} ({selectedUser.email})
                </p>
              </div>
              <button
                onClick={closeModal}
                className="text-gray-400 hover:text-gray-600 dark:hover:text-gray-200"
              >
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
            
            {modalLoading ? (
              <div className="p-8 text-center text-gray-500 dark:text-gray-400">
                加载中...
              </div>
            ) : (
              <div className="p-6 space-y-6">
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                  <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
                    <div className="text-sm text-gray-500 dark:text-gray-400">总学习时长</div>
                    <div className="text-xl font-bold text-gray-900 dark:text-white">
                      {formatTime(selectedUser.total_time_spent)}
                    </div>
                  </div>
                  <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
                    <div className="text-sm text-gray-500 dark:text-gray-400">已完成课程</div>
                    <div className="text-xl font-bold text-gray-900 dark:text-white">
                      {selectedUser.completed_lessons}
                    </div>
                  </div>
                  <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
                    <div className="text-sm text-gray-500 dark:text-gray-400">进行中</div>
                    <div className="text-xl font-bold text-gray-900 dark:text-white">
                      {selectedUser.in_progress_lessons}
                    </div>
                  </div>
                  <div className="bg-gray-50 dark:bg-gray-700 rounded-lg p-4">
                    <div className="text-sm text-gray-500 dark:text-gray-400">完成率</div>
                    <div className="text-xl font-bold text-gray-900 dark:text-white">
                      {selectedUser.completion_rate.toFixed(1)}%
                    </div>
                  </div>
                </div>
                
                <div>
                  <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                    各模块进度
                  </h3>
                  <div className="space-y-3">
                    {selectedUser.module_progress.map((module) => (
                      <div key={module.module_id} className="space-y-1">
                        <div className="flex justify-between text-sm">
                          <span className="text-gray-700 dark:text-gray-300 font-medium">
                            {module.module_name}
                          </span>
                          <span className="text-gray-500 dark:text-gray-400">
                            {module.completed}/{module.total} | {formatTime(module.time_spent)}
                          </span>
                        </div>
                        <div className="w-full bg-gray-200 dark:bg-gray-600 rounded-full h-2">
                          <div
                            className={`h-2 rounded-full ${getProgressColor(module.completed / module.total * 100)}`}
                            style={{ width: `${module.total > 0 ? (module.completed / module.total * 100) : 0}%` }}
                          />
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
                
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  <div>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                      学习日历（近30天）
                    </h3>
                    <div className="grid grid-cols-7 gap-1">
                      {['日', '一', '二', '三', '四', '五', '六'].map((day) => (
                        <div
                          key={day}
                          className="text-center text-xs text-gray-500 dark:text-gray-400 py-1"
                        >
                          {day}
                        </div>
                      ))}
                      {selectedUser.calendar_data.map((day, i) => (
                        <div
                          key={i}
                          className={`aspect-square rounded-sm flex items-center justify-center text-xs ${
                            day.lessons > 0
                              ? 'bg-green-500 text-white'
                              : day.time_spent > 0
                              ? 'bg-green-200 dark:bg-green-800 text-green-800 dark:text-green-200'
                              : 'bg-gray-100 dark:bg-gray-700 text-gray-400'
                          }`}
                          title={`${day.date}: ${day.lessons}课, ${day.time_spent}分钟`}
                        >
                          {new Date(day.date).getDate()}
                        </div>
                      ))}
                    </div>
                  </div>
                  
                  <div>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-4">
                      最近活动
                    </h3>
                    <div className="space-y-2 max-h-48 overflow-y-auto">
                      {selectedUser.recent_activities.length === 0 ? (
                        <p className="text-gray-500 dark:text-gray-400 text-sm">暂无活动记录</p>
                      ) : (
                        selectedUser.recent_activities.map((activity, i) => (
                          <div key={i} className="flex items-start gap-2 text-sm">
                            <span className={`px-2 py-0.5 rounded text-xs ${
                              activity.status === 'completed' 
                                ? 'bg-green-100 text-green-700 dark:bg-green-800 dark:text-green-200'
                                : 'bg-yellow-100 text-yellow-700 dark:bg-yellow-800 dark:text-yellow-200'
                            }`}>
                              {activity.status === 'completed' ? '完成' : '进行中'}
                            </span>
                            <div className="flex-1">
                              <div className="text-gray-900 dark:text-white font-medium">
                                {activity.lesson_title}
                              </div>
                              <div className="text-gray-500 dark:text-gray-400 text-xs">
                                {activity.module_name} | {formatTime(activity.time_spent)}
                              </div>
                            </div>
                          </div>
                        ))
                      )}
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {showGroupProgress && (
        <GroupProgressModal onClose={() => setShowGroupProgress(false)} />
      )}
    </div>
  )
}
