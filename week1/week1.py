import marimo

__generated_with = "0.16.5"
app = marimo.App(layout_file="layouts/week1.grid.json", css_file="style3.css")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objs as go
    return go, mo, np


@app.cell
def _(mo):
    # FIX: We define all styles ONCE globally. This stops the CSS from breaking dynamically.
    global_styles = mo.md("""
    <style>
      @keyframes blink { 50% { opacity: 0; } }
      .blink-red { animation: blink 1s step-start infinite; color: #e74c3c; font-weight: bold; }
      .blink-orange { animation: blink 1s step-start infinite; color: #e67e22; font-weight: bold; }
      .blink-green { animation: blink 1s step-start infinite; color: #2ecc71; font-weight: bold; }
      .blink-blue { animation: blink 1s step-start infinite; color: #3498db; font-weight: bold; }

      /* Unique and fancy break line */
      hr.fancy-line {
          border: 0;
          height: 3px;
          background-image: linear-gradient(to right, transparent, #2ecc71, #3498db, transparent);
          margin: 40px 0;
          border-radius: 5px;
      }
    </style>
    """)

    fancy_divider = mo.md("<hr class='fancy-line'>")
    return fancy_divider, global_styles


@app.cell
def _(global_styles, mo):
    _src = "../photos/me.jpg"

    # Left Side
    profile_image = mo.image(src=_src, width="180px",
                             height="180px", rounded=True)

    # Right Side
    profile_text = mo.md("""
    # Hi! I am Ahmed AlHennawi
    ### This is my Amazing CV
    """)

    # Horizontal layout for the header
    header = mo.vstack([
        global_styles,  # Inject CSS invisibly
        mo.hstack([profile_image, profile_text],
                  justify="start", align="center", gap="5rem")
    ])

    header
    return


@app.cell(hide_code=True)
def _(fancy_divider, mo):
    dob_title = mo.vstack([
        fancy_divider,
        mo.md("""
        ## 1. Date of birth
        Can you guess what year I was born?
        """)
    ])
    dob_title
    return


@app.cell
def _(mo, np):
    year = 2002
    numbers = np.arange(1950, 2007).tolist()
    dropdown = mo.ui.dropdown(
        options=numbers, value=1995, label="Born in:"
    )
    dropdown
    return (dropdown,)


@app.cell
def _(dropdown, mo):
    val = int(dropdown.value)

    # Using the global CSS classes now instead of breaking style tags!
    if val < 1989:
        content = mo.md(
            """<div class="blink-red">NOOOO i am not a grandfather lol</div>""")
    elif val < 2002:
        content = mo.md(
            """<div class="blink-orange">Do I Look That Old! lol</div>""")
    elif val == 2002:
        content = mo.md(
            """<div class="blink-green">🎉Congrats, You got it RIGHT🎉</div>""")
    else:
        content = mo.md(
            """<div class="blink-red">No Habibi, I'm Not A Teenager! lol</div>""")

    content
    return


@app.cell(hide_code=True)
def _(fancy_divider, mo):
    timeline_title = mo.vstack([
        fancy_divider,
        mo.md("""
        ## 2. My Study & Work Timeline
        """)
    ])
    timeline_title
    return


@app.cell
def _(mo):
    yearS = mo.ui.slider(2017, 2026, value=2020, label="Select Year:")

    controls_timeline = mo.hstack(
        [yearS], justify="start", gap="2rem")
    controls_timeline
    return (yearS,)


@app.cell
def _(mo, yearS):
    # Updated to use the clean global CSS classes
    if yearS.value == 2017:
        contentS = mo.md(f"""
        <h3> Access Scholarship (Year {yearS.value})</h3>
        <p>Starting My 2-Year English Scholarship Sponsored by the US Consulate!</p>
        <div class="blink-green">A Journey of Learning, Growth, and New Opportunities!</div>
        """)
    elif yearS.value == 2018:
        contentS = mo.md(f"""
        <h3>Lego Collaboration (Year {yearS.value})</h3>
        <p> Japan Sponsored My School, Providing us with LEGO kits and NXT devices to Build and Program Robots.</p>
        <div class="blink-blue">This is where I fell in love with coding.</div>
        """)
    elif yearS.value == 2019:
        contentS = mo.md(f"""
        <h3> The last year of High School (Year {yearS.value})</h3>
        <p> This is when i decided to study Multimedia </p>
        <div class="blink-red">I was so excited to start my life in University.</div>
        """)
    elif yearS.value == 2020:
        contentS = mo.md(f"""
        <h3> University of Palestine (Year {yearS.value})</h3>
        <p> This is when I began my undergraduate studies in Multimedia.</p>
        <div class="blink-orange">Where I expanded my skills in coding, design, and the broader world of technology </div>
        """)
    elif yearS.value == 2022:
        contentS = mo.md(f"""
        <h3> HTML Email Developer (Year {yearS.value})</h3>
        <p> This is when I learned MJML language</p>
        <div class="blink-orange">It was an interesting thing to learn </div>
        """)
    elif yearS.value == 2024:
        contentS = mo.md(f"""
        <h3>Graduation (Year {yearS.value})</h3>
        <p> This is when i graduated but sadly i could not do that much because of the war </p>
        <div class="blink-blue">I was so excited to Graduate! </div>
        """)
    elif yearS.value == 2025:
        contentS = mo.md(f"""
        <h3> Moved to London (Year {yearS.value})</h3>
        <p> It was nice to have this opportunity to come here </p>
        <div class="blink-green"> I was so Happy! </div>
        """)
    elif yearS.value == 2026:
        contentS = mo.md(f"""
        <h3> Msc Computer Science in UAL (Year {yearS.value})</h3>
        <p> Advancing my expertise in computer science at the University of the Arts London </p>
        <div class="blink-orange"> Coming soon! </div>
        """)
    else:
        contentS = mo.md(f"""
        <h3> This was a quiet year (Year {yearS.value})</h3>
        <p> Chilled Year</p>
        <div class="blink-blue">Nothing Interesting Happened </div>
        """)

    contentS
    return


@app.cell(hide_code=True)
def _(fancy_divider, mo):
    skills_title = mo.vstack([
        fancy_divider,
        mo.md("""
        ## 3. My Skill Chart
        """)
    ])
    skills_title
    return


@app.cell
def _(mo):
    yearP = mo.ui.slider(2018, 2025, value=2020, label="Choose Year:")
    yearP
    return (yearP,)


@app.cell
def _(go, mo, yearP):
    skills = {
        "Data Analytics": min(100, max(0, (yearP.value-2024)*7)),
        "Designing": min(100, (yearP.value-2016)*7 + 12),
        "Python": min(100, max(0, (yearP.value-2023)*25)),
        "HTML": min(100, max(0, (yearP.value-2020)*10 + 45)),
        "CSS": min(100, max(0, (yearP.value-2014)*5)),
        "Italian": min(100, max(0, (yearP.value-2022)*12)),
        "Cyber Security": min(100, max(0, (yearP.value-2024)*4)),
    }

    fig = go.Figure()

    # Radar chart
    fig.add_trace(go.Scatterpolar(
        r=list(skills.values()),
        theta=list(skills.keys()),
        fill='toself',
        name=f'Year {yearP.value}',
        marker=dict(color='rgba(26, 188, 156, 0.7)')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=True,
        title=f"Skills Overview - {yearP.value}",
        width=400,
        height=400
    )

    chart = mo.ui.plotly(fig)

    chart
    return


if __name__ == "__main__":
    app.run()
