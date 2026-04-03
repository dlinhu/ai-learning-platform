import api from './api'

export interface LoginResponse {
  access_token: string
  token_type: string
}

export interface User {
  id: string
  username: string
  email: string
  role: string
  group: string
  created_at: string
}

export const authApi = {
  async login(username: string, password: string): Promise<LoginResponse> {
    const params = new URLSearchParams()
    params.append('username', username)
    params.append('password', password)
    
    const response = await api.post<LoginResponse>('/auth/login', params, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    })
    return response.data
  },
  
  async register(username: string, email: string, password: string, group: string = 'group1'): Promise<User> {
    const response = await api.post<User>('/auth/register', {
      username,
      email,
      password,
      group
    })
    return response.data
  },
  
  async getMe(): Promise<User> {
    const response = await api.get<User>('/auth/me')
    return response.data
  }
}
