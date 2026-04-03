import api from './api'

export interface Module {
  id: string
  name: string
  description: string
  order_index: number
  lesson_count: number
  completed_count: number
}

export interface KnowledgePoint {
  id: string
  title: string
  description: string
  category: string
  importance: number
  related_terms: string[]
  related_knowledge: string[]
  examples: Array<{title: string; prompt: string; response: string}>
  key_concepts: string[]
  common_mistakes: string[]
  best_practices: string[]
  external_links: string[]
}

export interface Term {
  id: string
  term: string
  definition: string
  category: string
  examples: string[]
  related_terms: string[]
  detailed_definition: string
  related_concepts: string[]
  usage_examples: string[]
  external_links: string[]
}

export interface PracticeQuestion {
  id: string
  knowledge_point_id: string
  question_type: 'single_choice' | 'multiple_choice' | 'true_false' | 'fill_blank' | 'short_answer'
  question_text: string
  options: string[]
  correct_answer?: string
  explanation?: string
  difficulty: number
  order_index: number
}

export interface SubmitAnswerRequest {
  question_id: string
  user_answer: string
}

export interface SubmitAnswerResponse {
  is_correct: boolean
  correct_answer: string
  explanation: string
}

export interface PracticeProgress {
  total_questions: number
  answered_questions: number
  correct_answers: number
  progress_percentage: number
}

export interface Lesson {
  id: string
  module_id: string
  date: string
  title: string
  topics: string[]
  difficulty: string
  time_estimate: number
  materials: Material[]
  materials_count: number
  material_titles: string[]
  summary?: string
  progress_status: string
  knowledge_points: KnowledgePoint[]
  terms: Term[]
  structured_content?: LessonContent
}

 
export interface LessonContent {
  sections: LessonSection[]
}
 
export interface LessonSection {
  title: string
    content: string
    type: 'text' | 'code' | 'example' | 'summary'
    order: number
}

export interface Material {
  title: string
  text: string
  path: string
}

export interface Content {
  type: string
  html: string
  raw?: string
  error?: string
}

export interface TimelineItem {
  id: string
  module_id: string
  date: string
  title: string
  status: string
}

export const courseApi = {
  async getModules(): Promise<Module[]> {
    const response = await api.get<Module[]>('/courses/modules')
    return response.data
  },
  
  async getModule(id: string): Promise<Module> {
    const response = await api.get<Module>(`/courses/modules/${id}`)
    return response.data
  },
  
  async getModuleLessons(moduleId: string): Promise<Lesson[]> {
    const response = await api.get<Lesson[]>(`/courses/modules/${moduleId}/lessons`)
    return response.data
  },
  
  async getLesson(id: string): Promise<Lesson> {
    const response = await api.get<Lesson>(`/courses/lessons/${id}`)
    return response.data
  },
  
  async getContent(path: string): Promise<Content> {
    const response = await api.get<Content>(`/courses/content/${encodeURIComponent(path)}`)
    return response.data
  },
  
  async getTimeline(): Promise<TimelineItem[]> {
    const response = await api.get<TimelineItem[]>('/courses/timeline')
    return response.data
  },
  
  async getAllTerms(): Promise<Term[]> {
    const response = await api.get<Term[]>('/courses/terms')
    return response.data
  },
  
  async getTerm(id: string): Promise<Term> {
    const response = await api.get<Term>(`/courses/terms/${id}`)
    return response.data
  },
  
  async getPracticeQuestions(knowledgePointId: string): Promise<PracticeQuestion[]> {
    const response = await api.get<PracticeQuestion[]>(`/practice/knowledge-point/${knowledgePointId}`)
    return response.data
  },
  
  async submitAnswer(request: SubmitAnswerRequest): Promise<SubmitAnswerResponse> {
    const response = await api.post<SubmitAnswerResponse>('/practice/submit', request)
    return response.data
  },
  
  async getPracticeProgress(knowledgePointId: string): Promise<PracticeProgress> {
    const response = await api.get<PracticeProgress>(`/practice/progress/${knowledgePointId}`)
    return response.data
  }
}
