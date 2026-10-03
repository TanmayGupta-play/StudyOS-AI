# Study OS AI — Roadmap

We build in small steps. Each step: understand the concept -> write the code -> run it -> commit.

## Phase 1: Core build
- [ ] **Step 1: Project setup** - folder structure, FastAPI hello world, Postgres (pgvector) + Redis in Docker
- [ ] **Step 2: Database layer** - SQLAlchemy models, Alembic migrations, repository-service pattern
- [ ] **Step 3: Auth** - signup/login, password hashing, JWT
- [ ] **Step 4: Document upload + async jobs** - upload PDF, Redis queue, background worker
- [ ] **Step 5: RAG pipeline** - chunking, embeddings, pgvector search, answers that cite their sources
- [ ] **Step 6: First LLM tool-calling agent** - LangChain basics: tools, prompts, memory
- [ ] **Step 7: Specialist agents** - summarizer, quiz, flashcards, planner
- [ ] **Step 8: Multi-agent graph** - LangGraph supervisor that routes tasks to the agents
- [ ] **Step 9: Next.js frontend** - auth, upload, chat, flashcards, quizzes
- [ ] **Step 10: Deploy**

## Phase 2: Standout features
- FSRS spaced repetition, adaptive quizzes from a mastery model, study plan that updates itself,
  Socratic tutor mode, audio summaries, analytics dashboard, RAG/agent evaluation (RAGAS, LangSmith)
