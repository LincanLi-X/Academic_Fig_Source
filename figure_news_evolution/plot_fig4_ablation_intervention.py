from svg_utils import SVG, PALETTE, plot_axes, line_series, smooth_curve
DAYS=list(range(21))

def main():
    svg=SVG(1500,560); svg.text(750,42,'Figure 4 · Ablation and intervention analysis',30,'700')
    panels=[(70,'(a) Memory / role ablation'),(540,'(b) Agent-type ablation'),(1010,'(c) Early intervention')]
    # a: reductions are copied from original figure labels: -39.8%, -37.8%, -22.3%
    sx,sy=plot_axes(svg,panels[0][0],105,390,330,0,20,0,7,range(0,21,5),range(0,8,2),'Days','Average Deviation',panels[0][1])
    base=smooth_curve(1.8,6.38,7.34,15); no_mem=[round(v*(1-.398),2) for v in base]; no_role=[round(v*(1-.378),2) for v in base]; no_pra=[round(v*(1-.223),2) for v in base]
    for vals,c in [(base,PALETTE['blue']),(no_mem,PALETTE['red']),(no_role,PALETTE['teal']),(no_pra,PALETTE['gold'])]: line_series(svg,sx,sy,DAYS,vals,c,sw=2.6)
    for i,(lab,c) in enumerate([('FUSE',PALETTE['blue']),('w/o memory (-39.8%)',PALETTE['red']),('w/o role (-37.8%)',PALETTE['teal']),('w/o PRA (-22.3%)',PALETTE['gold'])]):
        svg.line(96,470+i*20,126,470+i*20,c,4); svg.text(134,475+i*20,lab,14,'700',anchor='start')
    # b
    sx,sy=plot_axes(svg,panels[1][0],105,390,330,0,20,0,7,range(0,21,5),range(0,8,2),'Days','Average Deviation',panels[1][1])
    series=[('Full roles',base,PALETTE['blue']),('No commentator',[v*.62 for v in base],PALETTE['red']),('No spreader',[v*.82 for v in base],PALETTE['gold']),('No verifier',[min(7,v*1.08) for v in base],PALETTE['purple']),('No bystander',[v*.94 for v in base],PALETTE['gray'])]
    for lab,vals,c in series: line_series(svg,sx,sy,DAYS,[round(v,2) for v in vals],c,sw=2.4)
    for i,(lab,_,c) in enumerate(series): svg.line(566,470+i*20,596,470+i*20,c,4); svg.text(604,475+i*20,lab,14,'700',anchor='start')
    # c exact table endpoints/no intervention vs intervention
    sx,sy=plot_axes(svg,panels[2][0],105,390,330,0,20,0,8,range(0,21,5),range(0,9,2),'Days','Average Deviation',panels[2][1])
    no_int=smooth_curve(1.841,6.383,7.340,15); inter=smooth_curve(1.841,4.559,5.302,4)
    line_series(svg,sx,sy,DAYS,no_int,PALETTE['red'],sw=3); line_series(svg,sx,sy,DAYS,inter,PALETTE['blue'],sw=3)
    svg.line(sx(4),sy(0),sx(4),sy(5.9),PALETTE['blue'],1.5,dash='5 5'); svg.text(sx(4)+8,sy(5.9),'official agent',14,'700',anchor='start',fill=PALETTE['blue'])
    svg.line(1050,472,1080,472,PALETTE['red'],4); svg.text(1088,477,'No intervention',15,'700',anchor='start')
    svg.line(1050,498,1080,498,PALETTE['blue'],4); svg.text(1088,503,'Intervention',15,'700',anchor='start')
    svg.save('figure_news_evolution/figures/fig4_ablation_intervention.svg')
if __name__=='__main__': main()
