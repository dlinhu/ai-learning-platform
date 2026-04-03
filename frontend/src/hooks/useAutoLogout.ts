import { useEffect, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import { useAuthStore } from '../stores/authStore'

const INACTIVITY_TIMEOUT = 10 * 60 * 1000 // 10分钟

export function useAutoLogout() {
  const { user, logout } = useAuthStore()
  const navigate = useNavigate()
  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  useEffect(() => {
    if (!user) return

    const resetTimer = () => {
      if (timerRef.current) clearTimeout(timerRef.current)
      timerRef.current = setTimeout(() => {
        logout()
        navigate('/login')
      }, INACTIVITY_TIMEOUT)
    }

    const events = ['mousedown', 'keydown', 'scroll', 'touchstart', 'mousemove']
    
    events.forEach(event => {
      window.addEventListener(event, resetTimer, true)
    })

    resetTimer()

    return () => {
      if (timerRef.current) clearTimeout(timerRef.current)
      events.forEach(event => {
        window.removeEventListener(event, resetTimer, true)
      })
    }
  }, [user, logout, navigate])
}
