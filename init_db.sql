-- Create signals table
CREATE TABLE IF NOT EXISTS signals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id VARCHAR NOT NULL,
  symbol VARCHAR NOT NULL,
  signal_type VARCHAR NOT NULL,
  confidence FLOAT,
  data JSONB,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create trades table
CREATE TABLE IF NOT EXISTS trades (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  symbol VARCHAR NOT NULL,
  entry_price FLOAT,
  exit_price FLOAT,
  position_size FLOAT,
  profit_loss FLOAT,
  agent_id VARCHAR,
  status VARCHAR DEFAULT 'open',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  closed_at TIMESTAMP
);

-- Create agent_metrics table
CREATE TABLE IF NOT EXISTS agent_metrics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  agent_id VARCHAR NOT NULL,
  agent_name VARCHAR,
  total_trades INT DEFAULT 0,
  profit_loss FLOAT DEFAULT 0,
  win_rate FLOAT DEFAULT 0,
  sharpe_ratio FLOAT DEFAULT 0,
  avg_holding_time INT DEFAULT 0,
  date DATE DEFAULT CURRENT_DATE,
  UNIQUE(agent_id, date)
);

-- Create agent_status table
CREATE TABLE IF NOT EXISTS agent_status (
  agent_id VARCHAR PRIMARY KEY,
  status VARCHAR DEFAULT 'idle',
  last_execution TIMESTAMP,
  error_count INT DEFAULT 0
);

-- Create dashboard_events table
CREATE TABLE IF NOT EXISTS dashboard_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  type VARCHAR,
  agent_id VARCHAR,
  data JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_signals_timestamp ON signals(timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_signals_symbol ON signals(symbol);
CREATE INDEX IF NOT EXISTS idx_trades_agent_id ON trades(agent_id);
CREATE INDEX IF NOT EXISTS idx_trades_symbol ON trades(symbol);
CREATE INDEX IF NOT EXISTS idx_dashboard_events_created_at ON dashboard_events(created_at DESC);

-- Create views
CREATE OR REPLACE VIEW agent_summary AS
SELECT 
  m.agent_id,
  m.agent_name,
  m.total_trades,
  m.profit_loss,
  m.win_rate,
  m.sharpe_ratio,
  s.status,
  s.last_execution
FROM agent_metrics m
LEFT JOIN agent_status s ON m.agent_id = s.agent_id;

