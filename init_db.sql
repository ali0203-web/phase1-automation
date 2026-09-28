-- Direct schema initialization
-- PostgreSQL will handle the IF NOT EXISTS clauses

-- 1. ORDERS TABLE
CREATE TABLE IF NOT EXISTS orders (
  id SERIAL PRIMARY KEY,
  order_id VARCHAR(255) UNIQUE NOT NULL,
  symbol VARCHAR(20) NOT NULL,
  side VARCHAR(10) NOT NULL,
  quantity DECIMAL(18, 8) NOT NULL,
  price DECIMAL(18, 8),
  order_type VARCHAR(20) NOT NULL,
  status VARCHAR(20) NOT NULL,
  broker VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  expires_at TIMESTAMP,
  retry_count INT DEFAULT 0,
  error_message TEXT,
  INDEX idx_symbol (symbol),
  INDEX idx_status (status),
  INDEX idx_broker (broker),
  INDEX idx_created_at (created_at)
);

-- 2. POSITIONS TABLE
CREATE TABLE IF NOT EXISTS positions (
  id SERIAL PRIMARY KEY,
  symbol VARCHAR(20) NOT NULL,
  broker VARCHAR(50) NOT NULL,
  quantity DECIMAL(18, 8) NOT NULL,
  average_cost DECIMAL(18, 8),
  current_price DECIMAL(18, 8),
  unrealized_pnl DECIMAL(18, 8),
  realized_pnl DECIMAL(18, 8),
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(symbol, broker),
  INDEX idx_symbol (symbol),
  INDEX idx_broker (broker)
);

-- 3. JOB_QUEUE TABLE
CREATE TABLE IF NOT EXISTS job_queue (
  id SERIAL PRIMARY KEY,
  job_id VARCHAR(255) UNIQUE NOT NULL,
  job_type VARCHAR(100) NOT NULL,
  status VARCHAR(50) NOT NULL,
  payload JSONB NOT NULL,
  priority INT DEFAULT 0,
  scheduled_for TIMESTAMP,
  started_at TIMESTAMP,
  completed_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX idx_status (status),
  INDEX idx_job_type (job_type),
  INDEX idx_priority (priority)
);

-- Verify tables were created
SELECT 'Database schema initialized successfully!' as status;
SELECT table_name FROM information_schema.tables WHERE table_schema='public' ORDER BY table_name;
