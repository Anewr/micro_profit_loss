import streamlit as st

st.set_page_config(page_title="Simple Micro Futures P&L Calculator")

# -------------------------
# Contract Specs (Simple)
# -------------------------
contracts = {
    "MES": {"tick_size": 0.25, "tick_value": 1.25},
    "MNQ": {"tick_size": 0.25, "tick_value": 0.50},
    "M2K": {"tick_size": 0.10, "tick_value": 0.50},
    "MYM": {"tick_size": 1.00, "tick_value": 0.50},
    "MCL": {"tick_size": 0.01, "tick_value": 1.00},

    # Micro FX (CME)
    "M6B": {"tick_size": 0.0001, "tick_value": 0.625},     # GBPUSD
    "M6E": {"tick_size": 0.00005, "tick_value": 0.625},    # EURUSD
    "M6J": {"tick_size": 0.0000005, "tick_value": 0.50},   # JPYUSD

    # Metals
    "MHG": {"tick_size": 0.0005, "tick_value": 0.50},      # Micro Copper
    "SIL": {"tick_size": 0.005, "tick_value": 5.00},       # Micro Silver
    "MGC": {"tick_size": 0.10, "tick_value": 1.00},
}

# -------------------------
# Title
# -------------------------
st.title("📊 Simple Micro Futures P&L Calculator (One Trade)")

# -------------------------
# Inputs
# -------------------------
contract = st.selectbox("Contract", list(contracts.keys()), key="contract_select")

entry = st.number_input("Entry Price", format="%.6f", key="entry_price")
stop = st.number_input("Stop-Loss Price", format="%.6f", key="stop_price")
target = st.number_input("Take-Profit Price", format="%.6f", key="target_price")

contracts_count = st.number_input("Number of Contracts", min_value=1, value=1, key="contract_count")

tick_size = contracts[contract]["tick_size"]
tick_value = contracts[contract]["tick_value"]

# -------------------------
# Calculations
# -------------------------
def calc_ticks(entry, price, tick_size):
    return (price - entry) / tick_size

stop_ticks = calc_ticks(entry, stop, tick_size)
target_ticks = calc_ticks(entry, target, tick_size)

stop_pl = stop_ticks * tick_value * contracts_count
target_pl = target_ticks * tick_value * contracts_count

# -------------------------
# Output
# -------------------------
st.subheader("📈 Results")

col1, col2 = st.columns(2)

with col1:
    st.metric("Loss at Stop", f"${stop_pl:,.2f}", delta=stop_pl)

with col2:
    st.metric("Profit at Target", f"${target_pl:,.2f}", delta=target_pl)

st.write(f"**Ticks to Stop:** {stop_ticks:.1f}")
st.write(f"**Ticks to Target:** {target_ticks:.1f}")
