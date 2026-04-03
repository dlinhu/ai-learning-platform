import api from './api'

export interface AdminStats {
  total_users: number
  active_users_today: number
  active_users_week: number
  total_time_spent: number
  avg_time_per_user: number
  total_completions: number
  avg_completion_rate: number
}

export interface UserListItem {
  user_id: string
  username: string
  email: string
  role: string
  group: string
  created_at: string
  total_time_spent: number
  completed_lessons: number
  in_progress_lessons: number
  completion_rate: number
  last_active: string | null
  current_streak: number
}

export interface UsersListResponse {
  users: UserListItem[]
  total: number
  page: number
  per_page: number
  total_pages: number
}

export interface ModuleProgressItem {
  module_id: string
  module_name: string
  completed: number
  total: number
  time_spent: number
}

export interface RecentActivity {
  lesson_id: string
  lesson_title: string
  module_name: string
  status: string
  time_spent: number
  completed_at: string | null
}

export interface CalendarDay {
  date: string
  time_spent: number
  lessons: number
}

export interface UserDetailResponse {
  user_id: string
  username: string
  email: string
  total_time_spent: number
  completed_lessons: number
  in_progress_lessons: number
  completion_rate: number
  module_progress: ModuleProgressItem[]
  recent_activities: RecentActivity[]
  calendar_data: CalendarDay[]
}

export interface UsersListParams {
  page?: number
  per_page?: number
  sort_by?: 'time_spent' | 'completion_rate' | 'last_active' | 'username'
  order?: 'asc' | 'desc'
  search?: string
}

export interface GroupMemberProgress {
  user_id: string
  username: string
  email: string
  role: string
  group: string
  total_time_spent: number
  completed_lessons: number
  in_progress_lessons: number
  completion_rate: number
  last_active: string | null
  current_streak: number
}

export interface GroupProgressResponse {
  group_name: string
  total_members: number
  members: GroupMemberProgress[]
}

export interface GroupSummary {
  group_name: string
  member_count: number
  total_time_spent: number
  total_completed: number
  total_in_progress: number
  admins: number
}


export const adminApi = {
  getStats: async (): Promise<AdminStats> => {
    const response = await api.get<AdminStats>('/admin/stats')
    return response.data
  },

  getUsers: async (params: UsersListParams = {}): Promise<UsersListResponse> => {
    const response = await api.get<UsersListResponse>('/admin/users', { params })
    return response.data
  },

  getUserDetail: async (userId: string): Promise<UserDetailResponse> => {
    const response = await api.get<UserDetailResponse>(`/admin/users/${userId}/detail`)
    return response.data
  },

  updateUserGroup: async (userId: string, group: string): Promise<{ message: string; group: string }> => {
    const response = await api.put<{ message: string; group: string }>(`/admin/users/${userId}/group`, null, {
      params: { group }
    })
    return response.data
  },

  updateUserRole: async (userId: string, role: string): Promise<{ message: string; role: string; username: string }> => {
    const response = await api.put<{ message: string; role: string; username: string }>(`/admin/users/${userId}/role`, null, {
      params: { role }
    })
    return response.data
  },

  getGroupProgress: async (groupName: string): Promise<GroupProgressResponse> => {
    const response = await api.get<GroupProgressResponse>(`/admin/groups/${groupName}/progress`)
    return response.data
  },

  getGroupsSummary: async (): Promise<{ groups: GroupSummary[] }> => {
    const response = await api.get<{ groups: GroupSummary[] }>('/admin/groups/summary')
    return response.data
  },


  getModules: async (): Promise<{ id: string; name: string; description: string; order_index: number; lesson_count: number }[]> => {
    const response = await api.get('/admin/modules')
    return response.data
  },

  createModule: async (name: string, description?: string): Promise<{ id: string; name: string; message: string }> => {
    const response = await api.post('/admin/modules', { name, description })
    return response.data
  },

  updateModule: async (moduleId: string, data: { name?: string; description?: string; order_index?: number }): Promise<{ message: string }> => {
    const response = await api.put(`/admin/modules/${moduleId}`, data)
    return response.data
  },

  deleteModule: async (moduleId: string): Promise<{ message: string }> => {
    const response = await api.delete(`/admin/modules/${moduleId}`)
    return response.data
  },

  updateLesson: async (lessonId: string, data: {
    title?: string
    topics?: string[]
    difficulty?: string
    time_estimate?: number
    summary?: string
    date?: string
  }): Promise<{ message: string }> => {
    const response = await api.put(`/admin/lessons/${lessonId}`, data)
    return response.data
  },

  deleteLesson: async (lessonId: string): Promise<{ message: string }> => {
    const response = await api.delete(`/admin/lessons/${lessonId}`)
    return response.data
  },

  createLesson: async (data: {
    module_id: string
    title: string
    date?: string
    topics?: string[]
    difficulty?: string
    time_estimate?: number
    summary?: string
    materials?: { title: string; path: string; type: string }[]
    raw_content?: string
  }): Promise<{ id: string; title: string; message: string }> => {
    const response = await api.post('/admin/lessons', data)
    return response.data
  },

  uploadLesson: async (moduleId: string, file: File, title?: string, date?: string): Promise<{
    id: string
    title: string
    summary: string
    topics: string[]
    difficulty: string
    time_estimate: number
    message: string
  }> => {
    const formData = new FormData()
    formData.append('file', file)
    if (title) formData.append('title', title)
    if (date) formData.append('date', date)
    
    const response = await api.post(`/admin/lessons/upload?module_id=${moduleId}`, formData, {
      headers: { 'Content-Type': 'multipart/form-data' }
    })
    return response.data
  },

  getAISettings: async (): Promise<{
    provider: string
    openai_api_key: string | null
    openai_base_url: string | null
    local_model_url: string | null
    local_model_name: string | null
  }> => {
    const response = await api.get('/admin/ai-settings')
    return response.data
  },

  updateAISettings: async (data: {
    provider: string
    openai_api_key?: string
    openai_base_url?: string
    local_model_url?: string
    local_model_name?: string
  }): Promise<{ message: string }> => {
    const response = await api.put('/admin/ai-settings', data)
    return response.data
  },

  testAISettings: async (data: {
    provider: string
    openai_api_key?: string
    openai_base_url?: string
    local_model_url?: string
    local_model_name?: string
  }): Promise<{ success: boolean; message: string }> => {
    const response = await api.post('/admin/ai-settings/test', data)
    return response.data
  }
}
