import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { useAuthStore } from './stores/authStore'
import Layout from './components/Layout'
import Home from './pages/Home'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import CourseList from './pages/CourseList'
import ModuleDetail from './pages/ModuleDetail'
import LessonDetail from './pages/LessonDetail'
import AdminDashboard from './pages/AdminDashboard'
import AdminCourses from './pages/AdminCourses'
import AdminAISettings from './pages/AdminAISettings'
import AdminArticles from './pages/AdminArticles'
import ArticleForm from './pages/ArticleForm'
import Articles from './pages/Articles'
import ArticleDetail from './pages/ArticleDetail'

function PrivateRoute({ children }: { children: React.ReactNode }) {
  const { user } = useAuthStore()
  return user ? <>{children}</> : <Navigate to="/login" />
}

function AdminRoute({ children }: { children: React.ReactNode }) {
  const { user } = useAuthStore()
  if (!user) return <Navigate to="/login" />
  if (user.role !== 'admin' && user.role !== 'group_admin') return <Navigate to="/dashboard" />
  return <>{children}</>
}

function SuperAdminRoute({ children }: { children: React.ReactNode }) {
  const { user } = useAuthStore()
  if (!user) return <Navigate to="/login" />
  if (user.role !== 'admin') return <Navigate to="/dashboard" />
  return <>{children}</>
}

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="dashboard" element={<PrivateRoute><Dashboard /></PrivateRoute>} />
          <Route path="courses" element={<PrivateRoute><CourseList /></PrivateRoute>} />
          <Route path="courses/:moduleId" element={<PrivateRoute><ModuleDetail /></PrivateRoute>} />
          <Route path="lesson/:id" element={<PrivateRoute><LessonDetail /></PrivateRoute>} />
          <Route path="articles" element={<PrivateRoute><Articles /></PrivateRoute>} />
          <Route path="articles/:id" element={<PrivateRoute><ArticleDetail /></PrivateRoute>} />
          <Route path="admin" element={<AdminRoute><AdminDashboard /></AdminRoute>} />
          <Route path="admin/courses" element={<SuperAdminRoute><AdminCourses /></SuperAdminRoute>} />
          <Route path="admin/ai-settings" element={<SuperAdminRoute><AdminAISettings /></SuperAdminRoute>} />
          <Route path="admin/articles" element={<SuperAdminRoute><AdminArticles /></SuperAdminRoute>} />
          <Route path="admin/articles/create" element={<SuperAdminRoute><ArticleForm /></SuperAdminRoute>} />
          <Route path="admin/articles/edit/:id" element={<SuperAdminRoute><ArticleForm /></SuperAdminRoute>} />
        </Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
