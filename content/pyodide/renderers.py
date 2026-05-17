import marimo

__generated_with = "0.23.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # JupyterLab Renderers
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## FASTA
    """)
    return


@app.cell
def _(display):
    def Fasta(data=''):
        bundle = {}
        bundle['application/vnd.fasta.fasta'] = data
        bundle['text/plain'] = data
        display(bundle, raw=True)

    Fasta(""">SEQUENCE_1
    MTEITAAMVKELRESTGAGMMDCKNALSETNGDFDKAVQLLREKGLGKAAKKADRLAAEG
    LVSVKVSDDFTIAAMRPSYLSYEDLDMTFVENEYKALVAELEKENEERRRLKDPNKPEHK
    IPQFASRKQLSDAILKEAEEKIKEELKAQGKPEKIWDNIIPGKMNSFIADNSQLDSKLTL
    MGQFYVMDDKKTVEQVIAEKEKEFGGKIKIVEFICFEVGEGLEKKTEDFAAEVAAQL
    >SEQUENCE_2
    SATVSEINSETDFVAKNDQFIALTKDTTAHIQSNSLQSVEELHSSTINGVKFEEYLKSQI
    ATIGENLVVRRFATLKAGANGVVNGYIHTNGRVGVVIAAACDSAEVASKSRDLLRQICMH""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## GeoJSON
    """)
    return


@app.cell
def _(display):
    def GeoJSON(data):
        bundle = {}
        bundle['application/geo+json'] = data
        bundle['text/plain'] = data
        display(bundle, raw=True)
    
    GeoJSON({
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [125.6, 10.1]
      },
      "properties": {
        "name": "Dinagat Islands"
      }
    })
    return


if __name__ == "__main__":
    app.run()

