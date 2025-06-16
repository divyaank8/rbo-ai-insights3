import streamlit as st
import time

# Static data

rm_daily_nudge_rbo3 = """
🏦 RM Daily Nudge – RBO-3 <br style="line-height: 0.5;">

🚀 <strong>Room to Improve</strong><br style="line-height: 0.5;">

Your region is currently ranked <strong>3rd</strong> in your AO (out of 5 RBOs), <strong>4th</strong> in your Network, and <strong>7th</strong> in your Circle.    
Performance has been mixed – CASA and Loan achievements hover around 60–65% of MTD targets. NPA is marginally above threshold, and there are multiple improvement opportunities across loans, deposits, and operations.<br style="line-height: 0.5;">
📈 <strong>Performance Overview</strong><br style="line-height: 0.5;">
💰 Deposits: Moderate CASA achievement, but several branches with <50% performance.
⬆️ Advances: Housing and SME Loans are lagging with low conversion and sourcing issues.
⚠️ NPA: Slightly elevated NPA levels with increasing stress in SME/Agri segments.<br style="line-height: 0.5;">
⚙️ Operational: ATM outages and Re-KYC pendency need proactive resolution.<br style="line-height: 0.5;">
📌 <strong>Suggested Focus</strong><br style="line-height: 0.5;">
🛠️ Strengthen CASA performance via local campaigns and corporate tie-ups.<br style="line-height: 0.5;">
📊 Improve loan conversion by addressing documentation gaps and faster TAT.<br style="line-height: 0.5;">
🚨 Contain NPA through early alerts and segment-wise resolution strategies.<br style="line-height: 0.5;">

🌟 <strong>Top Performing Branches</strong>:<br style="line-height: 0.5;">
Preet Vihar, Nehru Place<br style="line-height: 0.5;">
🔻 <strong>Bottom Performing Branches</strong>:<br style="line-height: 0.5;">
Laxmi Nagar, Shastri Nagar, Nangloi, Rani Bagh
"""

rm_daily_nudge_rbo3_deposits = """
💰 <strong>Deposits (CASA)</strong>
MTD: ₹10.8 Cr vs Target ₹18 Cr 🔹 60% Achieved – Room for growth.
⭐ <strong>Top Branches:</strong>  
Preet Vihar, Nehru Place, Krishna Nagar  
🔻<strong>Bottom Branches:</strong>  
Laxmi Nagar, Rani Bagh, Nangloi, Shastri Nagar
📌 <strong>Snapshot:</strong>
 • 12 branches <50% budget achievement
 • <strong>Persistent Laggards:</strong> Laxmi Nagar, Shastri Nagar, Rani Bagh  
 • <strong>New Declines:</strong> Nangloi – sudden ₹40L drop due to salary account shift
🛠️ <strong>Actions:</strong>
 • Hyper-local campaigns with tailored product positioning (e.g. senior citizen deposits, youth savings)  
 • Conduct CSP re-engagement at corporate hubs near Laxmi Nagar & Rani Bagh  
 • Address Nangloi shift: Engage lost corporate tie-up, offer relationship-led win-back strategy  
"""



rm_daily_nudge_rbo3_advances = """

⬆️ <strong>Advances (Total)</strong>
MTD: ₹8.2 Cr vs Target ₹14 Cr 🔹 59% Achieved
⭐ <strong>Top Branches:</strong>
Nehru Place, Preet Vihar
🔻 <strong>Bottom Branches:</strong>
Nangloi, Rani Bagh, Laxmi Nagar, Shastri Nagar

💼 <strong>SME Loans</strong>
MTD: ₹3.4 Cr vs Target ₹6 Cr 🔹 56% Achieved
⭐ <strong>Top Branches:</strong>
Nehru Place, Preet Vihar
🔻 <strong>Bottom Branches:</strong>
Nangloi, Laxmi Nagar, Rani Bagh
📌 <strong>Snapshot:</strong>
 • 4 branches <30% budget achievement; 15 >60%
 • <strong>Persistent Laggards:</strong>
   Nangloi, Rani Bagh
 • <strong>New Issues:</strong>
   Laxmi Nagar: Delays in collateral valuation, slow TAT
   Rani Bagh: No sourcing from Tri Nagar SME market
🛠️ <strong>Actions:</strong>
• <strong>All Laggards:</strong>
  Cluster outreach + focused SME RM deployment
• <strong>New Issues:</strong>
  • Laxmi Nagar: Engage approved valuers to reduce bottlenecks
  • Rani Bagh: Activate marketing in Tri Nagar cluster

🏠 <strong>Housing Loans</strong>
MTD: ₹3.9 Cr vs Target ₹7 Cr 🔹 55% Achieved
⭐ <strong>Top Branches:</strong>
Preet Vihar, Krishna Nagar
🔻 <strong>Bottom Branches:</strong>
Rani Bagh, Laxmi Nagar, Shastri Nagar
📌 <strong>Snapshot:</strong>
 • 3 branches <40% of target; 10 >65%
 • <strong>Persistent Laggards:</strong>
   Shastri Nagar, Rani Bagh
 • <strong>New Issues:</strong>
    Laxmi Nagar: Walk-ins shifting to HDFC due to faster turnaround
   Rani Bagh: 3 CIBIL-based rejections (<680 scores)
🛠️ <strong>Actions:</strong>
• <strong>All Laggards:</strong>
  Push digital onboarding; assign dedicated HL officer
• <strong>New Issues:</strong>
  • Laxmi Nagar: Match HDFC TAT; emphasize SBI benefits in branch comms
  • Rani Bagh: Run credit education + pre-check CIBIL clinic

🚗 <strong>Auto Loans</strong>
MTD: ₹1.65 Cr vs Target ₹3.5 Cr 🔹 47% Achieved
⭐ <strong>Top Branches:</strong>
Preet Vihar, Nehru Place
🔻 <strong>Bottom Branches:</strong>
Nangloi, Seelampur, Laxmi Nagar
📌 <strong>Snapshot:</strong>
 • 4 branches <30% of target; 12 >55%
 • <strong>Persistent Laggards:</strong>
   Nangloi, Laxmi Nagar
 • <strong>New Issues:</strong>
   Nangloi: No dealer partnerships; zero cases
   Seelampur: 2 leads lost to NBFC due to slow approvals
🛠️ <strong>Actions:</strong>
• <strong>All Laggards:</strong>
  Dealer tie-ups + incentive-based lead tracking
• <strong>New Issues:</strong>
  • Nangloi: Partner with local Hero dealer; provide weekend desk
  • Seelampur: Enable in-principle approval via branch fast lane
"""





rm_daily_nudge_rbo3_npa = """
⚠️ <strong>NPA Management</strong>
Current NPA: 1.91% 🔺 +12 bps vs Target 1.65% → ₹1.7 Cr total NPA
📌 <strong>Key Branches:</strong>
 • Nangloi: ₹0.22 Cr NPA (SME overdue 90+ days)
 • Rani Bagh: ₹0.18 Cr (personal loan NPA)
 • Shastri Nagar: ₹0.15 Cr Agri NPA
🛠️ <strong>Actions:</strong>
 • Launch aggressive recovery drives in SME/Agri backed by early-warning signals
 • Proactive restructuring for eligible borrowers (esp. SME)
 • Leverage legal notices in >90 day default cases
 • Introduce branch-level NPA tracker board with weekly RM reviews
"""

rm_daily_nudge_rbo3_ops = """
🏧 <strong>ATM & Operational Performance</strong>
Uptime: 94.2% vs Target 95% → 24 outages
🔻 <strong>Low Performing ATMs:</strong>
Laxmi Nagar, Shastri Nagar, Seelampur
📌 <strong>Issues:</strong>
 • Cashouts: Poor cash load forecasting in 4 branches
 • Uptime: Laxmi Nagar has 10+ outages due to old hardware
🛠️ <strong>Actions:</strong>
 • Replace outdated ATM hardware (Laxmi Nagar)
 • Deploy AI-based cash forecasting to reduce outages
 • Strengthen ATM vendor SLAs and conduct fortnightly reviews
 • Re-KYC pendency follow-up: Deploy interns for ground-level drives in Rani Bagh, Nangloi
"""













# RBO 1

rm_daily_nudge_rbo1 = """
🏦 RM Daily Nudge – RBO-1

🎉 <strong>Congratulations!</strong> 🏆  
Your Region is ranked <strong>2nd</strong> in your AO (out of 5 RBOs), <strong>3rd</strong> in your Network, and <strong>6th</strong> in your Circle.  
Your team has shown strong, consistent performance this month, maintaining steady CASA (89%) and Loan (65%) MTD budget achievements. However, the rising NPA trend (+18 bps) needs your urgent attention.  
📈 <strong>Performance Overview</strong>
💰 Deposits: You're at the highest budget achievement in your AO and Network.
⬆️ Advances: Achievements are close to being on track and should reach targets.
⚠️ NPA: The increase is a concern and is above the peer average.
⚙️ Operational: A few branches have shown operational lapses.  
📌 <strong>Suggested Focus</strong>
✅ Maintain momentum in CASA and Loans.
🚨 Aggressively tackle operational/compliance issues and NPA management.  
🌟 <strong>Top Performing Branches</strong>: 
New Delhi Main Branch (Parliament Street), Connaught Place
🔻 <strong>Bottom Performing Branches</strong>: 
Saket, Janakpuri, Dwarka Sector 10
"""

# 📊 Category-wise Deep Dive  

rm_daily_nudge_rbo1_deposits = """
💰 <strong>Deposits (CASA)</strong>
MTD: ₹16.02 Cr vs Target ₹18 Cr 🔹 89% Achieved – Strong performance.
⭐ <strong>Top Branches:</strong>
New Delhi Main, Connaught Place, Daryaganj
🔻<strong>Bottom Branches:</strong>
Badarpur, Connaught Place, Karol Bagh, Patel Nagar, Pitam Pura  
📌 <strong>Snapshot:</strong>
 • 8 branches <40% budget achievement; 28 branches >75% budget achievement
 • <strong>Persistent Laggards:</strong>
 Badarpur, Connaught Place, Karol Bagh + 3 others
 • <strong>New Declines:</strong>
   Patel Nagar: Lost major institutional account
   Pitam Pura: Salaried accounts moved due to better competitor package  
🛠️ <strong>Actions:</strong>
 • <strong>All Laggards</strong>: 
 Run hyper-local campaigns, tailor products to local needs
 • <strong>New Declines:</strong>
 Patel Nagar: Review & strengthen institutional client ties
 Pitam Pura: Deepen corporate engagement to retain salaried accounts

"""

rm_daily_nudge_rbo1_advances = """

⬆️ <strong>Advances (Total)</strong>
MTD: ₹9.75 Cr vs Target ₹15 Cr 🔹 65% Achieved
⭐ <strong>Top Branches:</strong>
New Delhi Main, Rohini Sec-7, Vasant Kunj
🔻 <strong>Bottom Branches:</strong>
Badarpur, Connaught Place, Karol Bagh, Patel Nagar, Dwarka Sec-10   
💼 <strong>SME Loans</strong>
MTD: ₹5.2 Cr vs Target ₹8 Cr 🔹 65% Achieved
⭐ <strong>Top Branches:</strong>
New Delhi Main Branch, Rohini Sec-7, Vasant Kunj
🔻 <strong>Bottom Branches:</strong>
Badarpur, Connaught Place, Karol Bagh, Patel Nagar, Dwarka Sec-10
📌 <strong>Snapshot:</strong> 
 • 5 branches <30% budget achievement; 20 >70% budget achievement
 • <strong>Persistent Laggards:</strong>
 Badarpur, Karol Bagh + 2 others
 • <strong>New Issues:</strong> 
   Dwarka Sec-10: High rejection rate (collateral/document gaps)
   Patel Nagar: TAT delays, disbursals lagging by 5 days
🛠️ <strong>Actions:</strong>
• <strong>All Laggards</strong>: 
    Run cluster-based outreach (e.g., “Loan Melas”), trade body engagement
 • <strong>New Issues:</strong>
 • Dwarka: Push CGTMSE-backed options
 • Patel Nagar: Fast-track high-ticket loans, optimize approval flow    
🏠 <strong>Housing Loans</strong>
MTD: ₹4.88 Cr vs Target ₹7.55 Cr 🔹 65% Achieved
⭐ <strong>Top Branches:</strong>
New Delhi Main, Rohini Sec-7, Vasant Kunj
🔻 <strong>Bottom Branches:</strong>
Badarpur, Connaught Place, Karol Bagh, Patel Nagar, Dwarka Sec-10
📌 <strong>Snapshot:</strong>
 • 6 branches <35% budget achievement
 • <strong>Persistent Laggards:</strong>
 Connaught Place, Laxmi Nagar + 1 (low market demand)
 • <strong>New Issues:</strong>
   Green Park: Lost key builder tie-up
   Tilak Nagar: Competitor edge (rate & speed) → 15% drop in apps
🛠️ <strong>Actions:</strong>
• <strong>All Laggards</strong>
Run home loan clinics, attend project launches, digitize onboarding
<strong>New Issues:</strong>
Green Park: Re-engage lost builder, pursue new ones
Tilak Nagar: Promote transparent rates (no-hidden charges), simplify process  

🚗 <strong>Auto Loans</strong>
MTD: ₹1.89 Cr vs Target ₹4.5 Cr 🔹 42% Achieved
⭐ <strong>Top Branches:</strong>
New Delhi Main, Rohini Sec-7, Vasant Kunj
🔻 <strong>Bottom Branches:</strong> Badarpur, Connaught Place, Karol Bagh, Patel Nagar, Dwarka Sec-10
📌 <strong>Snapshot:</strong>
 • 19 branches <30% budget achievement
 • <strong>Key Issues:</strong>
 Lost key dealerships to competitor (better incentives, faster disbursals)
 Slower approval → 2-day delay = dealer dissatisfaction
🛠️ <strong>Actions</strong>
 • Re-engage dealerships, improve incentives, reduce processing time
 • Train dealers, launch dealer-tier rewards
 • Deploy on-site loan officers for instant approvals
"""

rm_daily_nudge_rbo1_npa = """
⚠️ <strong>NPA Management</strong>
Current NPA: 1.83% 🔺 +18 bps vs Target 1.65% → ₹1.5 Cr total NPA  
⭐ <strong>Top Branches:</strong>
New Delhi Main, Rohini Sec-7, Vasant Kunj
🔻 <strong>Bottom Branches:</strong>
Saket, Narela, Dwarka Sec-10, Connaught Place
📌 <strong>Snapshot:</strong>
 • Saket: High NPA ₹0.18 Cr – recovery/appraisal gaps
 • Janakpuri: Personal Loan NPA ↑ ₹0.15 Cr
 • Narela: Agri NPA ↑ ₹0.10 Cr (seasonal)
 • Connaught Place: NPA% down, but actuals up ₹0.20 Cr – disbursement spike masking risk
🛠️ <strong>Actions:</strong>
 • Rapid reviews, restructure viable cases, recover others
 • Boost early warning triggers, tighten underwriting
 • Intensify collections, legal action, post-disbursal checks
"""

rm_daily_nudge_rbo1_ops = """
🏧 <strong>ATM Availability</strong>
Uptime: 96.5% vs Target 95% → 18 outages 🔺 Target <20
⭐ <strong>Top ATMs:</strong>
New Delhi Main, Karol Bagh, Civil Lines
🔻 <strong>Bottom ATMs:</strong>
Laxmi Nagar, Uttam Nagar
📌 <strong>Snapshot:</strong>
 • Laxmi Nagar: 15 outages – poor connectivity, old hardware
 • Sarojini Nagar, Shastri Nagar: Major cash-outs due to poor forecasting
🛠️ <strong>Actions:</strong>
 • Use volume-based forecasting for cash replenishment
 • Audit & upgrade outdated ATMs
 • Strengthen monitoring, review vendor for strict adherence to service
"""

# RBO 2

rm_daily_nudge_rbo2 = """
🏦 RM Daily Nudge – RBO‑2

📉 <strong>Alert!</strong>  
Your Region is ranked <strong>5th</strong> in your AO (out of 5 RBOs), <strong>12th</strong> in your Network, and <strong>18th</strong> in your Circle.  
Performance is lagging behind—CASA at 62%, Loan at 48% of MTD budgets. NPA is rising (+32 bps). Significant operational issues noted.  
📈 <strong>Performance Overview</strong>
💰 Deposits: Deep underperformance—many branches below 50% CASA achievement.
⬇️ Advances: Loan targets are far from being met.
⚠️ NPA: Worrying uptick, well above peer average.
⚙️ Operational: Widespread ATM outages and Re‑KYC compliance issues.  
📌 <strong>Suggested Focus</strong>
🚨 Rapid recovery campaigns for deposits and loans.
🔧 Immediate fixes on ATMs & KYC compliance.
👥 Reinforce branch-level accountability.  
🌟 <strong>Top Performing Branches</strong>:
Vasant Vihar, Malviya Nagar
🔻 <strong>Bottom Performing Branches</strong>:
Badarpur, Narela, Trilokpuri
"""

# 📊 Category‑wise Deep Dive  

rm_daily_nudge_rbo2_deposits = """
💰 <strong>Deposits (CASA)</strong>
MTD: ₹11.5 Cr vs Target ₹18.5 Cr 🔹 62% Achieved – Underwhelming 
⭐ <strong>Top Branches:</strong>  
Vasant Vihar, Malviya Nagar  
🔻 <strong>Bottom Branches:</strong>  
Badarpur, Narela, Trilokpuri, Ghazipur, Shaheen Bagh  
📌 <strong>Snapshot:</strong>  
 • 6 branches <45% budget achievement  
 • <strong>Persistent Underperformance:</strong>  
Badarpur, Narela, Ghazipur  
 • <strong>New Declines:</strong>  
Trilokpuri: Lost a large corporate account  
Shaheen Bagh: Salaried accounts shifting due to competitor offers  
🛠️ <strong>Actions:</strong>  
 • <strong>Persistent Laggards:</strong> 
Micro‑market campaigns, targeted relationship management  
 • <strong>New Declines:</strong>  
Trilokpuri: Re‑negotiate with institution, offer customized CASA benefits  
Shaheen Bagh: Run CSP retention drives and promote digital salary credits  
"""

rm_daily_nudge_rbo2_advances = """

⬆️ <strong>Advances (Total)</strong>
MTD: ₹7.2 Cr vs Target ₹15 Cr 🔹 48% Achieved – Lagging
⭐ <strong>Top Branches:</strong>
Vasant Vihar, Malviya Nagar
🔻 <strong>Bottom Branches:</strong>
Badarpur, Narela, Trilokpuri, Ghazipur, Shaheen Bagh   
💼 <strong>SME Loans</strong>
MTD: ₹2.8 Cr vs Target ₹7 Cr 🔹 40% Achieved
⭐ <strong>Top Branches:</strong>
Vasant Vihar, Malviya Nagar, Janakpuri
🔻 <strong>Bottom Branches:</strong>
Badarpur, Karol Bagh (persistent), Dwarka Sec-10, Patel Nagar
📌 <strong>Snapshot:</strong>
 • 5 branches <30% budget achievement; 20 >70% budget achievement
 • <strong>Persistent Laggards:</strong>
Badarpur, Karol Bagh + 2 others
 • <strong>New Issues:</strong>
Dwarka Sec-10: High rejection rate (collateral/document gaps)
Patel Nagar: TAT delays, disbursals lagging by 5 days
🛠️ <strong>Actions:</strong>
 • <strong>All Laggards</strong>: 
Run cluster-based outreach (e.g., “Loan Melas”), trade body engagement
 • <strong>New Issues:</strong>
Dwarka: Push CGTMSE-backed options
Patel Nagar: Fast-track high-ticket loans, optimize approval flow  

🏠 <strong>Housing Loans</strong>
MTD: ₹3.1 Cr vs Target ₹8 Cr 🔹 39% Achieved
⭐ <strong>Top Branches:</strong>
Vasant Vihar, Malviya Nagar, Lajpat Nagar
🔻 <strong>Bottom Branches:</strong>
Ghazipur, Narela (persistent); Karol Bagh, Dwarka Sec-10
📌 <strong>Snapshot:</strong>
 • 5 branches <30% budget achievement; 4 branches >70%
 • <strong>Persistent Laggards:</strong>
Ghazipur, Narela + 2 others
 • <strong>New Issues:</strong>
   Karol Bagh: Builder tie-up fallout
   Dwarka Sec-10: Slow approvals due to back-office overload
🛠️ <strong>Actions:</strong>
 • <strong>All Laggards</strong>: 
Run on-ground housing loan camps with local builders
 • <strong>New Issues:</strong>
Karol Bagh: Rebuild developer relations, offer rate-matching
Dwarka: Augment back-office team; set SLA-based routing  

🚗 <strong>Auto Loans</strong>
MTD: ₹1.5 Cr vs Target ₹4 Cr 🔹 38% Achieved
⭐ <strong>Top Branches:</strong>
Vasant Vihar, Malviya Nagar, Connaught Place
🔻 <strong>Bottom Branches:</strong>
Badarpur, Narela (persistent); Shaheen Bagh, Patel Nagar
📌 <strong>Snapshot:</strong>
 • 6 branches <35% achievement; 19 >70%
 • <strong>Persistent Laggards:</strong>
   Badarpur, Narela + 2 others
 • <strong>New Issues:</strong>
Shaheen Bagh: Dealership tie-up expired
Patel Nagar: Disbursement delays post-sanction
🛠️ <strong>Actions:</strong>
 • <strong>All Laggards</strong>: 
 Organize "Drive SBI" weekend camps with top dealers
 • <strong>New Issues:</strong>
Shaheen Bagh: Renew dealer tie-ups, offer bundled schemes
Patel Nagar: Streamline post-sanction disbursement with SLA tracking
"""

rm_daily_nudge_rbo2_npa = """
⚠️<strong>NPA Management:</strong>
Current NPA: 1.82% 🔺 +32 bps vs Target 1.50%  
⭐ <strong>Top:</strong> Vasant Vihar, Malviya Nagar
🔻 <strong>Bottom:</strong> Badarpur, Narela, Trilokpuri, Ghazipur
📌 <strong>Snapshot:</strong>
 • Badarpur: SME & Personal loan defaults rising sharply
 • Trilokpuri: Agri‑NPA up ₹0.12 Cr (seasonal stress)
 • Ghazipur: Decline in NPA% but a rise in absolute NPA amounts  
🛠️ <strong>Actions:</strong>  
 • Finalize restructuring for viable borrowers, escalate recovery  
 • Publish monthly Early Warning reports  
 • Boost legal recovery team and set target SLAs  
"""

rm_daily_nudge_rbo2_ops = """
🏧 <strong>ATM Availability</strong>
Uptime: 94% vs Target 95%  25 outages 🔺 Target <20
⭐ <strong>Top ATMs:</strong> Vasant Vihar, Malviya Nagar
🔻 <strong>Bottom ATMs:</strong> Badarpur, Narela, Ghazipur, Trilokpuri
📌 <strong>Snapshot:</strong>
 • Badarpur: Recurrent hardware failures, no backup
 • Ghazipur: Frequent cash‑outs, forecasting errors 
🛠️ <strong>Actions:</strong>
 • Install backup UPS and upgrade failing ATMs
 • Conduct power and network diagnostics
<br>
🗂️ <strong>Re‑KYC Compliance</strong>
Re‑KYC Backlog: 350+ accounts pending
🛑 <strong>Issues:</strong>
 • Understaffed branches leading to documentation delays
 • Low online KYC uptake
🛠️ <strong>Actions:</strong>
 • Launch branch‑assisted digital KYC camps
 • Train staff teams to guide customers through digital process
"""




# Dictionary mapping for easy handling
rbo_summaries = {
    "RBO-1": rm_daily_nudge_rbo1,
    "RBO-2": rm_daily_nudge_rbo2,
    "RBO-3": rm_daily_nudge_rbo3,
}

rbo_deep_dives = {
    "RBO-3": {
        "Deposits": rm_daily_nudge_rbo3_deposits,
        "Advances": rm_daily_nudge_rbo3_advances,
        "Operations": rm_daily_nudge_rbo3_ops,
        "NPA": rm_daily_nudge_rbo3_npa,

    },
        "RBO-1": {
        "Deposits": rm_daily_nudge_rbo1_deposits,
        "Advances": rm_daily_nudge_rbo1_advances,
        "Operations": rm_daily_nudge_rbo1_ops,
        "NPA": rm_daily_nudge_rbo1_npa,

    },
        "RBO-2": {
        "Deposits": rm_daily_nudge_rbo2_deposits,
        "Advances": rm_daily_nudge_rbo2_advances,
        "Operations": rm_daily_nudge_rbo2_ops,
        "NPA": rm_daily_nudge_rbo2_npa,

    },

}

# 💡 Icon mapping for deep dive sections
deep_dive_icons = {
    "Deposits": "💰",
    "Advances": "⬆️",
    "NPA & Ops": "🛠️",
    "NPA": "📉",
    "Cross-Sell & Digital": "📱",
    "Compliance": "✅",
}




# --- Page Configuration ---
st.set_page_config(
    page_title="SBI RBO IntelliAI",
    page_icon=":bank:",
    layout="wide"
)

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
            background-color: #edf4fa;
            color: #002B5B;
            font-family: 'Segoe UI', sans-serif;
            margin: 0 !important;
            padding: 0 !important;
        }


        .sbi-header {
            background-color: #002B5B;
            padding: 12px 40px; /* Added horizontal padding */
            border-radius: 0; /* Remove border radius for full-width block */
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 5px;
            width: 100vw; /* Full viewport width */
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .sbi-header img {
            height: 60px;
            margin-right: 20px;
        }

        .sbi-header-title {
            font-size: 30px;
            font-weight: 700;
            color: #ffffff;
        }

        .sbi-subtitle {
            font-size: 16px;
            color: #cce6ff;
            margin-top: 4px;
        }

        .stButton>button {
            background-color: #0072BC;
            color: white;
            font-weight: 600;
            font-size: 15px;
            padding: 12px 20px;
            border-radius: 8px;
            border: none;
            width: 100%;
        }

        .stButton>button:hover {
            background-color: #005A96;
        }

        .centered-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            margin-top: 0px;
        }

        h1, h2, h3 {
            color: #002B5B;
        }

        .chat-container {
            padding: 15px 20px;
            background-color: #ffffff;
            border: 1px solid #dbe4f0;
            border-radius: 10px;
            margin-top: 10px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.05);
        }

        .chat-bubble.bot {
            background-color: #eef5fc;
            color: #002B5B;
            padding: 10px 15px;
            border-radius: 10px;
            margin-bottom: 10px;
            font-size: 15px;
        }

        .back-btn-container {
            display: flex;
            justify-content: flex-start;
            margin-bottom: 1rem;
        }
        .back-btn-container button {
            width: auto !important;
            min-width: 120px;
            padding: 0.3rem 0.75rem;
            font-size: 0.9rem;
            border-radius: 6px;
        }
        
        
        
            button span {
        display: inline-block;
        width: 100%;
        text-align: center;
    }
    
        

        </style>

        
    

""", unsafe_allow_html=True)

# --- SBI Header Block ---
st.markdown("""
    <div class="sbi-header">
        <img src="https://upload.wikimedia.org/wikipedia/commons/c/cc/SBI-logo.svg" alt="SBI Logo">
        <div>
            <div class="sbi-header-title">SBI RBO IntelliAI</div>
            <div class="sbi-subtitle">Smart GenAI Insights</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- Page Routing with Session State ---
if "page" not in st.session_state:
    st.session_state.page = "home"

# --- Navigation: Homepage ---
if st.session_state.page == "home":
    st.markdown("""
        <div style="text-align: center; padding-top: 10px; padding-bottom: 20px;">
            <h3>👋 Welcome to your RBO IntelliAI Assistant</h3>
            <p style="font-size: 16px;">
                Choose a Regional Business Office to start a smart, insight-driven conversation about its performance and opportunities.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- Horizontally aligned RBO Buttons with Equal Width ---
    col1, col2, col3 = st.columns(3)
    rbo_names = ["RBO-1", "RBO-2", "RBO-3"]
    rbo_cols = [col1, col2, col3]

    for col, rbo in zip(rbo_cols, rbo_names):
        with col:
            if st.button(rbo):
                st.session_state.selected_rbo = rbo
                st.session_state.page = "chat"
                st.session_state.show_spinner = True  # 🔁 Reset spinner every time

                st.rerun()
                
                
                
                
                
                
                
                
  # --- CHAT PAGE ---
  
  
  
# --- CHAT PAGE ---
elif st.session_state.page == "chat":

    rbo = st.session_state.get("selected_rbo", "RBO-1")  # Default for demo

    if st.button("🔙", key="go_back_hidden", help="Go Back to Home"):
        # ✅ Reset the deep dive selections
        st.session_state.selected_deep_dive = None  # Reset selected dive
        st.session_state.chat_log = []

        st.session_state.page = "home"
        st.rerun()
           
        

    st.markdown(f"#### 💬 IntelliAI Chat for {rbo}")

    if st.session_state.get("show_spinner", True):
        with st.spinner(f"Typing {rbo}..."):
            time.sleep(1.5)
        st.session_state.show_spinner = False
        st.rerun()
    else:
        with st.container():
            st.markdown(f"""
                <div class="chat-container">
                    <div class="chat-bubble bot">
                        {rbo_summaries.get(rbo, 'No summary available.')}

            """, unsafe_allow_html=True)

    if rbo in rbo_deep_dives:

        deep_dive_options = list(rbo_deep_dives[rbo].keys())

        # Initialize session state for chat log
        if "chat_log" not in st.session_state:
            st.session_state.chat_log = []

        if "selected_deep_dives" not in st.session_state:
            st.session_state.selected_deep_dives = []

        # Inject styles
        st.markdown("""
        <style>
            .chat-container {
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
                padding: 15px 20px;
                background-color: #ffffff;
                border: 1px solid #dbe4f0;
                border-radius: 10px;
                margin-top: 10px;
                box-shadow: 0 1px 4px rgba(0,0,0,0.05);
            }

            .chat-bubble {
                padding: 10px 15px;
                border-radius: 12px;
                max-width: 85%;
                word-wrap: break-word;
                font-size: 15px;
            }

            .chat-bubble.bot {
                align-self: flex-start;
                background-color: #eef5fc;
                color: #002B5B;
            }

            .chat-bubble.user {
                align-self: flex-end;
                background-color: #d9fdd3;
                color: #002B5B;
            }

            .stButton > button {
                padding: 0.4rem 0.6rem;
                font-size: 0.83rem;
                margin: 2px;
                border-radius: 6px;
            }
        </style>
        """, unsafe_allow_html=True)


        
# --- Render chat log ---
        for dive in st.session_state.chat_log:
            icon = deep_dive_icons.get(dive, "📂")
            response = rbo_deep_dives[rbo].get(dive, "No insights available.")
            st.markdown(f"""
                <div class="chat-container">
                    <div class="chat-bubble user">{icon} {dive}</div>
                    <div class="chat-bubble bot">{response}</div>
                </div>
            """, unsafe_allow_html=True)

        # --- Buttons to select deep dives ---
        st.markdown('<div class="chat-section-title" style="margin-top: 20px;">Select a Segment for Detailed Insight:</div>', unsafe_allow_html=True)

        cols = st.columns(len(deep_dive_options), gap="small")
        for i, dive in enumerate(deep_dive_options):
            with cols[i]:
                icon = deep_dive_icons.get(dive, "📂")
                label = f"{icon} {dive}"
                if st.button(label, key=f"btn_{dive}", use_container_width=True):
                    st.session_state.chat_log.append(dive)
                    st.rerun()