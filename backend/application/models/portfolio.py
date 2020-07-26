from application.extensions import db
from sqlalchemy import Numeric
from sqlalchemy.dialects.postgresql import JSONB, UUID


class Portfolio(db.Model):
    __tablename__ = "portfolio"

    id = db.Column(db.Integer(), db.Sequence("portfolio_id_seq"), primary_key=True)
    name = db.Column(db.String(50), nullable=True, server_default="Default")
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id", ondelete="CASCADE"))

    user = db.relationship("User", back_populates="portfolios")
    stocks = db.relationship("Stock", secondary="portfolio_stocks")


class Stock(db.Model):
    __tablename__ = "stocks"

    id = db.Column(db.Integer(), db.Sequence("stocks_id_seq"), primary_key=True)
    ticker = db.Column(db.String(15), unique=True)
    short_name = db.Column(db.String(255))
    info = db.Column(JSONB)

    history = db.relationship("StockHistory", backref="stock", uselist=True)


class StockHistory(db.Model):
    id = db.Column(db.Integer(), db.Sequence("stock_history_id_seq"), primary_key=True)
    stock_id = db.Column(db.Integer(), db.ForeignKey("stocks.id", ondelete="CASCADE"))
    date = db.Column(db.DateTime())
    close = db.Column(Numeric)
    open = db.Column(Numeric)
    high = db.Column(Numeric)
    low = db.Column(Numeric)
    dividends = db.Column(Numeric)
    volume = db.Column(Numeric)


class PortfolioStocks(db.Model):
    __tablename__ = "portfolio_stocks"

    id = db.Column(db.Integer(), primary_key=True)
    portfolio_id = db.Column(db.Integer(), db.ForeignKey("portfolio.id", ondelete="CASCADE"))
    stock_id = db.Column(db.Integer(), db.ForeignKey("stocks.id", ondelete="CASCADE"))
