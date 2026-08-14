"""
CHALLENGE: Build a Streamlit Dashboard
======================================

You've described the tips data, plotted it, and tested it. Everything so far has
lived in a notebook that only you can run. This challenge turns it into a thing
you can send someone a link to: a real dashboard, with filters and charts that
respond to clicks.

Streamlit's whole trick is that there's no web development involved. You write
ordinary Python, top to bottom, and Streamlit turns it into a page.

HOW TO RUN THIS
---------------
    pip install streamlit seaborn
    streamlit run streamlit_dashboard_challenge.py

It opens in your browser. Leave it running: every time you save this file,
hit "Rerun" in the browser (or turn on "Always rerun") and your changes appear.
That save-and-see loop is the nicest part of building with Streamlit.

WHAT YOU NEED
-------------
    tips.csv, in the same folder as this file.

HOW THIS FILE WORKS
-------------------
Six parts, gentle to solid to bonus. Fill in each "--- YOUR CODE ---" block in
order, saving as you go. The app runs at every stage, so you always see what
you just built.

All the worked solutions are at the very bottom, under a big SOLUTIONS banner.
They're inside a quoted block so they don't run, you have to go and look.
Have a real go at each part first.
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tips Dashboard", layout="wide")
sns.set_theme()

df = pd.read_csv("tips.csv")


# =============================================================================
# THE BIG IDEA, read this before you start
# =============================================================================
# Streamlit re-runs this entire file, top to bottom, every single time you touch
# a widget. There's no "onclick" handler to write, no state to wire up.
#
# A widget is just a function that returns the user's current choice:
#
#     day = st.selectbox("Pick a day", ["Sat", "Sun"])
#
# On the first run, `day` is "Sat". The user picks "Sun", the whole script runs
# again, and this time `day` is "Sun". That's it. That's the entire model.


def dashboard_page():
    """Parts 1 to 4 all live in here."""

    # -------------------------------------------------------------------------
    # PART 1 , Your first page                                        (gentle)
    # -------------------------------------------------------------------------
    # Lesson:
    #   st.title(text)      puts a big heading on the page
    #   st.write(anything)  is the swiss army knife , text, numbers, dataframes
    #   st.dataframe(df)    shows a scrollable, sortable table
    #
    # TASK 1.1: give the page a title.
    # TASK 1.2: write a line of text under it saying what the dashboard is for.
    #
    # --- YOUR CODE (Part 1) ---

    # -------------------------------------------------------------------------
    # PART 2 , Filters in the sidebar                                 (gentle)
    # -------------------------------------------------------------------------
    # Lesson:
    #   Putting st.sidebar. in front of any widget moves it to the left panel,
    #   which is where filters belong. A multiselect returns a LIST of choices:
    #
    #       picked = st.sidebar.multiselect("Day", options, default=options)
    #
    #   Then you filter the dataframe with .isin(), exactly like pandas.
    #
    # TASK 2.1: add a sidebar header (st.sidebar.header).
    # TASK 2.2: add a multiselect for 'day'. Use the unique days as both the
    #           options and the default, so everything is selected to start.
    # TASK 2.3: add a second multiselect for 'time'.
    # TASK 2.4: build `view` , df filtered down to the picked days and times.
    #           (hint: df[df["day"].isin(days) & df["time"].isin(times)])
    #
    # Part 2 replaces the line below. Until then, the rest of the app just
    # uses the full dataset.
    view = df

    # --- YOUR CODE (Part 2) ---

    # A filtered dataframe can end up empty, and every chart below would then
    # explode. Guarding against it early is a habit worth having.
    if view.empty:
        st.warning("No rows match those filters. Widen them to see the dashboard.")
        return

    # -------------------------------------------------------------------------
    # PART 3 , Headline numbers                                        (solid)
    # -------------------------------------------------------------------------
    # Lesson:
    #   st.metric(label, value) draws a big number with a caption, the classic
    #   dashboard tile. st.columns(3) splits the page into three side-by-side
    #   slots, and you draw into each one:
    #
    #       c1, c2, c3 = st.columns(3)
    #       c1.metric("Tables", 244)
    #
    #   These are the descriptive statistics you already know, on a page.
    #
    # TASK 3.1: split the page into three columns.
    # TASK 3.2: show the number of rows in `view`, the mean total_bill, and the
    #           median tip. Format the money ones nicely, e.g.
    #           f"${view['total_bill'].mean():.2f}"
    #
    # --- YOUR CODE (Part 3) ---

    # -------------------------------------------------------------------------
    # PART 4 , The chart chooser                                       (solid)
    # -------------------------------------------------------------------------
    # This is the heart of the dashboard, and it's a design lesson as much as a
    # coding one.
    #
    # The Financial Times' graphics team publish a "Visual Vocabulary", which
    # organises chart types by the RELATIONSHIP you want to show rather than by
    # what the chart looks like. Their nine categories are: deviation,
    # correlation, ranking, distribution, change over time, part-to-whole,
    # magnitude, spatial and flow. You pick the relationship that matters in
    # your story first, then choose a chart from within that category.
    #     https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary
    #
    # So instead of asking "what chart do you want?", this dashboard asks
    # "what are you trying to show?" and only then offers suitable charts.
    # Two dropdowns, where the second depends on the first.
    #
    # Notice that RELATIONSHIPS below only has six of the FT's nine categories.
    # tips has no dates, no locations and nothing flowing between states, so
    # three of them simply cannot be answered by this data. That's not a gap in
    # the dashboard, it's the dashboard being honest about its dataset.
    #
    # TASK 4.1: add a subheader for this section.
    # TASK 4.2: add a selectbox for the relationship. The options are the KEYS
    #           of RELATIONSHIPS (hint: list(RELATIONSHIPS)).
    # TASK 4.3: add a second selectbox for the chart type, whose options are
    #           RELATIONSHIPS[relationship] , the list for whatever they picked.
    # TASK 4.4: call draw_chart(view, chart) to render it.
    # TASK 4.5: put the UNAVAILABLE explanations inside an st.expander so
    #           curious users can see why three categories are missing.
    #
    # --- YOUR CODE (Part 4) ---

    # A nice finishing touch: let people see the actual filtered rows.
    with st.expander("See the filtered data"):
        st.dataframe(view)


# =============================================================================
# The chart definitions for Part 4.
# =============================================================================
# RELATIONSHIPS maps an FT category to the charts that can express it.
RELATIONSHIPS = {
    "Distribution": ["Histogram", "Box plot", "Violin plot"],
    "Correlation": ["Scatter plot"],
    "Ranking": ["Ordered bar"],
    "Magnitude": ["Grouped bar"],
    "Part-to-whole": ["Pie chart", "Stacked bar"],
    "Deviation": ["Diverging bar"],
}

# The three FT categories this dataset cannot support, and why.
UNAVAILABLE = {
    "Change over Time": "tips has no date column, only a day label",
    "Spatial": "there is no location or map data",
    "Flow": "nothing moves between states here",
}


def draw_chart(view, chart):
    """Draw whichever chart was chosen.

    Two ways of drawing appear here, and both are worth knowing.

    Streamlit's own charts (st.bar_chart) are one-liners that take a Series or
    DataFrame and are interactive for free. Great when the shape of your data
    already matches the chart.

    seaborn charts give you everything you learned in the plotting challenges.
    The pattern is always the same three lines:

        fig, ax = plt.subplots()     make a figure
        sns.something(..., ax=ax)    draw onto it
        st.pyplot(fig)               hand it to Streamlit

    Always plt.close(fig) afterwards, or a long session slowly eats memory.
    """
    # TASK 4.6: fill in the branches below. Two are done for you as a pattern,
    #           one seaborn and one native. Add the rest as you go , you don't
    #           need all nine working before you move on to Part 5.

    if chart == "Histogram":
        # A worked example: the seaborn pattern.
        fig, ax = plt.subplots()
        sns.histplot(data=view, x="total_bill", bins=25, ax=ax)
        ax.set_title("Distribution of total_bill")
        st.pyplot(fig)
        plt.close(fig)

    elif chart == "Ordered bar":
        # A worked example: the native pattern. Sort first, and the ranking
        # reads straight off the chart.
        ranked = view.groupby("day")["total_bill"].mean().sort_values(ascending=False)
        st.bar_chart(ranked)

    # --- YOUR CODE (Part 4.6) ---
    # Box plot     , sns.boxplot of total_bill by day
    # Violin plot  , sns.violinplot of total_bill by time
    # Scatter plot , sns.regplot of total_bill against tip
    # Grouped bar  , sns.barplot of total_bill by day, hue="time"
    # Pie chart    , matplotlib ax.pie of view["day"].value_counts()
    # Stacked bar  , st.bar_chart of pd.crosstab(view["day"], view["time"])
    # Diverging bar, each day's mean bill minus the overall mean, as ax.barh

    else:
        st.info("That chart isn't built yet. Add it in Part 4.6.")


# =============================================================================
# PART 5 , A second page: the tip calculator                            (solid)
# =============================================================================
# Lesson:
#   Not every page is charts. Streamlit's input widgets make little tools easy:
#
#       st.number_input(label, min_value=..., value=..., step=...)
#       st.slider(label, min, max, default)
#
#   Both return the current value, so you just do the maths with them.
#
# TASK 5.1: give the page a title.
# TASK 5.2: add a number_input for the bill, a slider for the tip percentage
#           (0 to 30, default 15), and a number_input for how many people are
#           splitting it (minimum 1).
# TASK 5.3: work out the tip, the total, and the amount per person.
# TASK 5.4: show all three as metrics in three columns.
# TASK 5.5 (nice touch): compare the tip against df["tip"].mean() and show
#           st.success() or st.info() depending on which is bigger.

def calculator_page():
    # --- YOUR CODE (Part 5) ---
    pass


# =============================================================================
# PART 6 , Wiring it into a multi-page app                              (bonus)
# =============================================================================
# This is the final boss, and it's shorter than you'd expect.
#
# Modern Streamlit builds multi-page apps out of functions. You wrap each page
# function in st.Page, hand the list to st.navigation, and run it:
#
#     pg = st.navigation([
#         st.Page(some_function, title="Shown in the menu", default=True),
#         st.Page(another_function, title="Second page"),
#     ])
#     pg.run()
#
# Streamlit draws the page switcher itself. One of them needs default=True.
#
# TASK 6.1: replace the dashboard_page() call below with an st.navigation setup
#           listing both dashboard_page and calculator_page.
#
# --- YOUR CODE (Part 6) ---
dashboard_page()


# =============================================================================
# =============================================================================
#
#                                S O L U T I O N S
#
# Everything below is inside a quoted block, so it does not run. Copy what you
# need out of it, but have a proper go at each part first , wrestling a layout
# into shape is most of how this sticks.
#
# =============================================================================
# =============================================================================

SOLUTIONS = '''

PART 1 , Your first page
------------------------
    st.title("Tips Dashboard")
    st.write("Filter the data on the left, then pick what you want to show.")


PART 2 , Filters in the sidebar
-------------------------------
    st.sidebar.header("Filters")
    days = st.sidebar.multiselect(
        "Day",
        sorted(df["day"].unique()),
        default=sorted(df["day"].unique()),
    )
    times = st.sidebar.multiselect(
        "Time",
        sorted(df["time"].unique()),
        default=sorted(df["time"].unique()),
    )
    view = df[df["day"].isin(days) & df["time"].isin(times)]

    Delete the placeholder "view = df" line once this is in.
    Watch the metrics and charts update as you tick boxes , every widget click
    re-runs the whole file, and everything downstream recalculates itself.


PART 3 , Headline numbers
-------------------------
    c1, c2, c3 = st.columns(3)
    c1.metric("Tables", len(view))
    c2.metric("Average bill", f"${view['total_bill'].mean():.2f}")
    c3.metric("Median tip", f"${view['tip'].median():.2f}")

    With no filters applied you should see 244 tables, an average bill of
    $19.79 and a median tip of $2.90 , the same numbers you calculated in the
    descriptive statistics challenge.


PART 4 , The chart chooser
--------------------------
    st.subheader("Chart explorer")
    relationship = st.selectbox("What do you want to show?", list(RELATIONSHIPS))
    chart = st.selectbox("Chart type", RELATIONSHIPS[relationship])
    draw_chart(view, chart)

    with st.expander("Why are some relationships missing?"):
        for name, reason in UNAVAILABLE.items():
            st.write(f"**{name}** , {reason}")

    The second selectbox rebuilds itself whenever the first one changes,
    because RELATIONSHIPS[relationship] is looked up fresh on every re-run.
    You get dependent dropdowns for free, with no event handling at all.


PART 4.6 , The remaining charts
-------------------------------
    elif chart == "Box plot":
        fig, ax = plt.subplots()
        sns.boxplot(data=view, x="day", y="total_bill", ax=ax)
        ax.set_title("total_bill by day")
        st.pyplot(fig)
        plt.close(fig)

    elif chart == "Violin plot":
        fig, ax = plt.subplots()
        sns.violinplot(data=view, x="time", y="total_bill", ax=ax)
        ax.set_title("total_bill by time")
        st.pyplot(fig)
        plt.close(fig)

    elif chart == "Scatter plot":
        fig, ax = plt.subplots()
        sns.regplot(data=view, x="total_bill", y="tip", ax=ax)
        ax.set_title("total_bill vs tip")
        st.pyplot(fig)
        plt.close(fig)

    elif chart == "Grouped bar":
        fig, ax = plt.subplots()
        sns.barplot(data=view, x="day", y="total_bill", hue="time",
                    errorbar=None, ax=ax)
        ax.set_title("Average total_bill by day and time")
        st.pyplot(fig)
        plt.close(fig)

    elif chart == "Pie chart":
        shares = view["day"].value_counts()
        fig, ax = plt.subplots()
        ax.pie(shares, labels=shares.index, autopct="%1.1f%%")
        ax.set_title("Share of tables by day")
        st.pyplot(fig)
        plt.close(fig)

    elif chart == "Stacked bar":
        crosstab = pd.crosstab(view["day"], view["time"])
        st.bar_chart(crosstab)

    elif chart == "Diverging bar":
        means = view.groupby("day")["total_bill"].mean()
        deviation = means - view["total_bill"].mean()
        fig, ax = plt.subplots()
        colours = ["tab:red" if v < 0 else "tab:blue" for v in deviation]
        ax.barh(deviation.index.astype(str), deviation.values, color=colours)
        ax.axvline(0, color="black", linewidth=1)
        ax.set_title("Each days average bill vs the overall average")
        st.pyplot(fig)
        plt.close(fig)

    The diverging bar is the one worth studying. Deviation charts always need a
    reference point, and here it is the overall mean bill. Subtracting it turns
    four similar-looking averages into a clear above/below picture.


PART 5 , The tip calculator
---------------------------
def calculator_page():
    st.title("Tip Calculator")
    bill = st.number_input("Bill amount ($)", min_value=0.0, value=20.0, step=1.0)
    pct = st.slider("Tip percentage", 0, 30, 15)
    people = st.number_input("Split between", min_value=1, value=2, step=1)

    tip = bill * pct / 100
    total = bill + tip

    c1, c2, c3 = st.columns(3)
    c1.metric("Tip", f"${tip:.2f}")
    c2.metric("Total", f"${total:.2f}")
    c3.metric("Each person pays", f"${total / people:.2f}")

    typical = df["tip"].mean()
    if tip > typical:
        st.success(f"That is above the dataset average tip of ${typical:.2f}.")
    else:
        st.info(f"The dataset average tip is ${typical:.2f}.")

    With the defaults ($20 bill, 15%) you get a $3.00 tip, a $23.00 total and
    $11.50 each. Note the min_value=1 on the people input, it stops anyone
    dividing by zero without you writing a single check.


PART 6 , Multi-page navigation
------------------------------
    pg = st.navigation([
        st.Page(dashboard_page, title="Dashboard", default=True),
        st.Page(calculator_page, title="Tip Calculator"),
    ])
    pg.run()

    Replace the bare dashboard_page() call with this. A page switcher appears in
    the sidebar, and note that you pass the FUNCTION ITSELF, dashboard_page with
    no brackets. With brackets you would call it immediately and hand st.Page
    the result instead of the function.


GOING FURTHER
-------------
    - Put @st.cache_data above a function that loads data, and Streamlit will
      only read the file once instead of on every single re-run.
    - st.download_button lets people export the filtered data as a CSV.
    - Streamlit Community Cloud will host this from a GitHub repo for free,
      which turns the whole thing into a link you can actually send someone.

'''