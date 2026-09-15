BTC Trading Data Export
=======================

Exported at: 2026-09-01T10:44:51.318Z
Format: JSON (one file per selected dataset)
Schema version: 2
All timestamps are UTC ISO 8601 values.
See manifest.json for applied filters, row counts, field definitions, relationships, and ML guidance.

market_intervals.json: 24481 rows - Time-ordered BTC OHLC and tick-derived market features. This is the main feature table for market-pattern modelling.
algorithm_evaluations.json: 49347 rows - Persisted algorithm decisions and their input snapshots. Use evaluatedAt to align a decision with market data.
trade_lots.json: 72 rows - Simulated position lifecycle records, from entry through exit. Closed lots contain outcome and P&L labels useful for supervised learning.
trade_events.json: 177 rows - Execution-level simulated buy/sell events. Join lotId to tradeLots.id to reconstruct a position's fills and costs.
trading_settings.json: 1 rows - Simulated-trading configuration records ordered by last update. These are explanatory inputs, not market observations.
