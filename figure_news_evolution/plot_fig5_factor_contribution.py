from svg_utils import SVG, PALETTE
import math
TOTAL={'SS':17.2,'NII':18.0,'CS':14.0,'STS':17.5,'TS':11.0,'PD':22.3}
TOPICS={
 'Politics':[18,19,14,17,10,22], 'Terrorism':[19,18,13,17,11,22],
 'Science':[13,27,16,12,7,25], 'Urban legends':[16,15,12,20,14,23], 'Finance':[15,18,18,16,12,21]
}
COLORS={'SS':'#D88F8A','NII':'#E2B857','CS':'#5DB7A4','STS':'#8E75B8','TS':'#6B7280','PD':'#2F5D8C'}

def arc(cx,cy,r,a0,a1):
    x0=cx+r*math.cos(a0); y0=cy+r*math.sin(a0); x1=cx+r*math.cos(a1); y1=cy+r*math.sin(a1)
    large=1 if a1-a0>math.pi else 0
    return f'M {cx},{cy} L {x0:.2f},{y0:.2f} A {r},{r} 0 {large},1 {x1:.2f},{y1:.2f} Z'

def main():
    svg=SVG(1280,680); svg.text(640,45,'Figure 5 · FUSE-EVAL factor contributions',30,'700')
    svg.rect(55,90,470,510,'white','#DDD7CB',rx=14); svg.text(290,126,'(a) Overall contribution',22,'700')
    start=-math.pi/2; cx,cy,r=290,335,170
    for k,v in TOTAL.items():
        a1=start+2*math.pi*v/100; svg.path(arc(cx,cy,r,start,a1),fill=COLORS[k],stroke='white',sw=2); mid=(start+a1)/2
        svg.text(cx+(r+30)*math.cos(mid),cy+(r+30)*math.sin(mid)+5,f'{k} {v:g}%',15,'700',fill=COLORS[k]); start=a1
    svg.circle(cx,cy,82,PALETTE['bg'],stroke='white',sw=2); svg.text(cx,cy-5,'100%',30,'700'); svg.text(cx,cy+25,'deviation',17,fill=PALETTE['muted'])
    svg.rect(570,90,655,510,'white','#DDD7CB',rx=14); svg.text(897,126,'(b) Topic-specific contribution profiles',22,'700')
    labels=list(TOTAL.keys()); x0,y0=700,180; barw=430; rowh=72
    for i,(topic,vals) in enumerate(TOPICS.items()):
        y=y0+i*rowh; svg.text(680,y+22,topic,15,'700',anchor='end')
        x=x0
        for lab,val in zip(labels,vals):
            w=barw*val/100; svg.rect(x,y,w,34,COLORS[lab],rx=3); 
            if val>=14: svg.text(x+w/2,y+23,lab,12,'700',fill='white')
            x+=w
        svg.text(x0+barw+12,y+23,'100%',12,anchor='start',fill=PALETTE['muted'])
    for i,lab in enumerate(labels):
        x=650+i*88; svg.rect(x,555,18,18,COLORS[lab],rx=3); svg.text(x+25,570,lab,14,'700',anchor='start')
    svg.save('figure_news_evolution/figures/fig5_factor_contribution.svg')
if __name__=='__main__': main()
