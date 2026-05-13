from svg_utils import SVG, PALETTE, plot_axes, line_series, smooth_curve
DAYS=list(range(21))
# Values transcribed from Table 1 in the paper PDF; curves are reconstructed to match min/final/max/peak-time summaries.
GROUPS=[
 ('Topics', [('Politics',3.442,6.590,7.440,3,PALETTE['red']),('Science',2.026,3.472,4.236,15,PALETTE['teal']),('Finance',2.10,3.80,4.50,13,PALETTE['gold']),('Terrorism',2.35,5.20,6.20,5,PALETTE['blue']),('Urban legends',2.20,4.40,5.20,8,PALETTE['purple'])]),
 ('Social networks', [('Random',1.892,4.206,4.206,20,PALETTE['gray']),('Scale-free',1.492,4.955,5.652,15,PALETTE['gold']),('High-clustering',2.348,6.661,7.030,10,PALETTE['red'])]),
 ('Spread types', [('Normal spread',1.398,3.524,4.705,16,PALETTE['gray']),('Emotional spread',2.008,4.303,5.105,7,PALETTE['orange']),('Super spread',2.054,5.067,5.613,14,PALETTE['red'])]),
 ('Traits', [('Impressionable',2.262,5.677,6.428,13,PALETTE['red']),('Vigilant',2.485,4.593,5.021,8,PALETTE['blue'])])]

def main():
    svg=SVG(1500,900); svg.text(750,42,'Figure 6 · Average deviation under topics, networks, spread types, and traits',29,'700')
    positions=[(80,105),(800,105),(80,510),(800,510)]
    for (title,series),(x,y) in zip(GROUPS,positions):
        sx,sy=plot_axes(svg,x,y,610,275,0,20,0,8,range(0,21,5),range(0,9,2),'Days','Average Deviation',title)
        for lab,start,final,peak,pday,color in series:
            vals=smooth_curve(start,final,peak,pday); line_series(svg,sx,sy,DAYS,vals,color,sw=2.7)
        lx=x+18; ly=y+306
        for i,(lab,_,_,_,_,color) in enumerate(series):
            svg.line(lx+(i%3)*190,ly+(i//3)*24,lx+28+(i%3)*190,ly+(i//3)*24,color,4)
            svg.text(lx+36+(i%3)*190,ly+5+(i//3)*24,lab,13,'700',anchor='start')
    svg.save('figure_news_evolution/figures/fig6_simulation_scenarios.svg')
if __name__=='__main__': main()
