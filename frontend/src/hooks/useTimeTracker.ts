import { useEffect, useRef, useCallback } from 'react'
import api from '../services/api'

interface TimeTrackerOptions {
  lessonId: string
  onSaveInterval?: number
  onVisibilityChange?: boolean
}

export function useTimeTracker({ 
  lessonId, 
  onSaveInterval = 300000,
  onVisibilityChange = true 
}: TimeTrackerOptions) {
  const startTimeRef = useRef<Date | null>(null)
  const totalTimeRef = useRef<number>(0)
  const saveIntervalRef = useRef<ReturnType<typeof setInterval> | null>(null)
  const isTrackingRef = useRef<boolean>(false)

  const saveTime = useCallback(async (additionalTime: number) => {
    if (additionalTime <= 0) return
    
    try {
      await api.post('/progress/update-time', {
        lesson_id: lessonId,
        time_spent: Math.floor(additionalTime / 60000),
        action: 'study'
      })
    } catch (error) {
      console.error('Failed to save time:', error)
    }
  }, [lessonId])

  const startTracking = useCallback(() => {
    if (isTrackingRef.current) return
    
    startTimeRef.current = new Date()
    isTrackingRef.current = true
  }, [])

  const stopTracking = useCallback(() => {
    if (!isTrackingRef.current || !startTimeRef.current) return
    
    const endTime = new Date()
    const sessionTime = endTime.getTime() - startTimeRef.current.getTime()
    totalTimeRef.current += sessionTime
    
    saveTime(sessionTime)
    
    startTimeRef.current = null
    isTrackingRef.current = false
  }, [saveTime])

  const handleVisibilityChange = useCallback(() => {
    if (document.hidden) {
      stopTracking()
    } else {
      startTracking()
    }
  }, [startTracking, stopTracking])

  const handleBeforeUnload = useCallback(() => {
    if (isTrackingRef.current && startTimeRef.current) {
      const endTime = new Date()
      const sessionTime = endTime.getTime() - startTimeRef.current.getTime()
      
      navigator.sendBeacon(
        '/api/progress/update-time',
        JSON.stringify({
          lesson_id: lessonId,
          time_spent: Math.floor(sessionTime / 60000),
          action: 'study'
        })
      )
    }
  }, [lessonId])

  useEffect(() => {
    startTracking()

    if (onVisibilityChange) {
      document.addEventListener('visibilitychange', handleVisibilityChange)
    }

    window.addEventListener('beforeunload', handleBeforeUnload)

    if (onSaveInterval > 0) {
      saveIntervalRef.current = setInterval(() => {
        if (isTrackingRef.current && startTimeRef.current) {
          const currentTime = new Date()
          const sessionTime = currentTime.getTime() - startTimeRef.current.getTime()
          
          saveTime(sessionTime)
          
          totalTimeRef.current += sessionTime
          startTimeRef.current = currentTime
        }
      }, onSaveInterval)
    }

    return () => {
      stopTracking()
      
      if (onVisibilityChange) {
        document.removeEventListener('visibilitychange', handleVisibilityChange)
      }
      
      window.removeEventListener('beforeunload', handleBeforeUnload)
      
      if (saveIntervalRef.current) {
        clearInterval(saveIntervalRef.current)
      }
    }
  }, [lessonId, onSaveInterval, onVisibilityChange, startTracking, stopTracking, handleVisibilityChange, handleBeforeUnload, saveTime])

  return {
    totalTime: totalTimeRef.current,
    isTracking: isTrackingRef.current
  }
}
