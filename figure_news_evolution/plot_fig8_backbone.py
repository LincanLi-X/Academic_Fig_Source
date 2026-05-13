from svg_utils import SVG, PALETTE, plot_axes, line_series
DAYS=list(range(21))
# Exact values reconstructed from vector coordinates embedded in the original Figure 8 PDF form.
GPT4O_MINI=[2.32,1.49,3.45,3.59,3.76,5.45,4.66,5.21,5.53,4.84,5.09,5.42,6.03,6.23,6.18,5.69,6.59,5.50,4.89,4.62,4.32]
GPT4=[2.92,1.82,4.27,4.21,4.10,4.72,4.92,5.11,4.47,4.16,4.97,5.42,5.63,5.58,5.09,5.99,4.91,5.28,5.69,5.73,5.17]

def main():
    svg=SVG(1000,650); svg.text(500,50,'Figure 8 · Different Backbone',32,'700')
    sx,sy=plot_axes(svg,90,105,800,410,0,20,1.5,6.8,range(0,21,2),[2,3,4,5,6],'Days','Average Deviation','GPT-4o-mini and GPT-4 preserve the accumulation effect')
    line_series(svg,sx,sy,DAYS,GPT4O_MINI,PALETTE['red'],sw=3); line_series(svg,sx,sy,DAYS,GPT4,PALETTE['blue'],marker='triangle',sw=3)
    svg.rect(620,420,220,70,'white','#DDD7CB',rx=10); svg.line(645,445,685,445,PALETTE['red'],4); svg.circle(665,445,5,PALETTE['red']); svg.text(700,451,'GPT-4o-mini',16,'700',anchor='start')
    svg.line(645,480,685,480,PALETTE['blue'],4); svg.path('M 665,474 L 658,487 L 672,487 Z',fill=PALETTE['blue'],stroke='white'); svg.text(700,486,'GPT-4',16,'700',anchor='start')
    svg.save('figure_news_evolution/figures/fig8_backbone.svg')
if __name__=='__main__': main()
