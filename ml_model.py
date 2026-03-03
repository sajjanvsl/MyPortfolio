import yfinance as yf
import pandas as pd
import ta
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def clean_dataframe(df):
    """
    Fix MultiIndex + 2D column issue from yfinance
    """

    # Flatten MultiIndex columns if present
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    required_cols = ["Open", "High", "Low", "Close", "Volume"]
    df = df[required_cols]

    # Force pure 1D columns
    for col in required_cols:
        df[col] = pd.Series(df[col].values.flatten(), index=df.index)

    return df


def train_model(stock="RELIANCE.NS"):

    df = yf.download(
        stock,
        period="2y",
        auto_adjust=True,
        progress=False,
        group_by="column"
    )

    if df.empty:
        return None, 0

    df = clean_dataframe(df)

    # Indicators
    df["EMA20"] = ta.trend.ema_indicator(close=df["Close"], window=20)
    df["EMA50"] = ta.trend.ema_indicator(close=df["Close"], window=50)
    df["RSI"] = ta.momentum.rsi(close=df["Close"], window=14)

    # Target
    df["Return"] = df["Close"].pct_change().shift(-1)
    df["Target"] = (df["Return"] > 0).astype(int)

    df.dropna(inplace=True)

    X = df[["EMA20", "EMA50", "RSI"]]
    y = df["Target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, shuffle=False, test_size=0.3
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, round(accuracy * 100, 2)
