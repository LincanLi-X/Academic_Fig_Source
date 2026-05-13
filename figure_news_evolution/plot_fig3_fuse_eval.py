from svg_utils import SVG, PALETTE, plot_axes, line_series

DAYS = list(range(21))
DIMENSIONS = {
    'SS':  [0.8,1.0,1.6,2.1,2.9,3.2,3.4,3.7,3.9,4.2,4.4,4.7,4.9,5.2,5.4,5.6,5.8,6.0,6.1,6.2,6.3],
    'NII': [0.6,1.2,2.0,3.0,3.8,4.4,4.9,5.3,5.6,5.9,6.1,6.3,6.6,6.8,7.0,7.1,7.2,7.3,7.4,7.4,7.5],
    'CS':  [0.7,0.9,1.4,2.0,2.5,3.1,3.6,3.9,4.2,4.5,4.8,5.1,5.3,5.5,5.7,5.9,6.0,6.1,6.2,6.3,6.4],
    'STS': [0.5,0.8,1.2,1.9,2.6,3.3,3.9,4.4,4.8,5.2,5.5,5.8,6.0,6.2,6.4,6.5,6.6,6.7,6.8,6.9,7.0],
    'TS':  [0.4,0.5,0.8,1.1,1.5,1.9,2.2,2.5,2.8,3.0,3.2,3.4,3.6,3.8,3.9,4.0,4.1,4.2,4.3,4.4,4.5],
    'PD':  [0.9,1.5,2.4,3.5,4.4,5.1,5.6,6.0,6.3,6.6,6.8,7.0,7.2,7.4,7.6,7.7,7.9,8.0,8.1,8.2,8.3],
}
COLORS = ['#D88F8A','#E2B857','#5DB7A4','#8E75B8','#6B7280','#2F5D8C']

def main():
    svg = SVG(1300, 720)
    svg.text(650, 48, 'Figure 3 · FUSE-EVAL cumulative deviation and case evolution', 30, '700')
    sx, sy = plot_axes(svg, 80, 110, 700, 460, 0, 20, 0, 9, range(0,21,4), range(0,10,2), 'Days', 'FUSE-EVAL score', '(a) Multi-dimensional deviation accumulation')
    for (name, vals), color in zip(DIMENSIONS.items(), COLORS):
        line_series(svg, sx, sy, DAYS, vals, color, name, sw=3)
    for i,(name,color) in enumerate(zip(DIMENSIONS.keys(), COLORS)):
        x=120+(i%3)*180; y=620+(i//3)*34
        svg.line(x,y-5,x+32,y-5,color,4); svg.circle(x+16,y-5,4,color); svg.text(x+42,y,name,16,'700',anchor='start')
    # case panel
    x0,y0,w,h = 835,112,390,455
    svg.rect(x0,y0,w,h,fill='white',stroke='#DDD7CB',rx=14)
    svg.text(x0+w/2,y0+34,'(b) A case of stepwise deception',22,'700')
    cards=[('Day 0 · true news','#EAF4EA','Trump was attacked at a campaign rally; eyewitnesses reported an ear injury.'),
           ('Day 8 · partially false','#FFF3D8','Some users speculate the incident may have been exaggerated for political effect.'),
           ('Day 20 · fake news','#FCE6E4','Trump was not attacked; it was staged as a dramatic campaign performance.')]
    for i,(title,fill,body) in enumerate(cards):
        yy=y0+72+i*126
        svg.rect(x0+26,yy,w-52,94,fill=fill,stroke='#E2DDD2',rx=12)
        svg.text(x0+44,yy+28,title,17,'700',anchor='start',fill=PALETTE['ink'])
        # simple wrapping
        words=body.split(); lines=[]; cur=''
        for wd in words:
            if len(cur)+len(wd)>48: lines.append(cur); cur=wd
            else: cur=(cur+' '+wd).strip()
        lines.append(cur)
        for j,line in enumerate(lines): svg.text(x0+44,yy+56+j*20,line,15,anchor='start',fill=PALETTE['muted'])
        if i<2: svg.text(x0+w/2, yy+116, '↓', 28, '700', fill='#777')
    svg.save('figure_news_evolution/figures/fig3_fuse_eval.svg')
if __name__ == '__main__': main()
