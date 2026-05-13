from __future__ import annotations
import math, os

PALETTE = {
    'red': '#D88F8A', 'blue': '#2F5D8C', 'teal': '#5DB7A4', 'gold': '#E2B857',
    'purple': '#8E75B8', 'green': '#7CBF7A', 'gray': '#6B7280', 'orange': '#E68A3F',
    'bg': '#FBFAF7', 'grid': '#E6E2DA', 'ink': '#222222', 'muted': '#666666'
}

def esc(s):
    return str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

class SVG:
    def __init__(self, w=1000, h=650):
        self.w=w; self.h=h; self.items=[]
        self.defs=[]
        self.add(f'<rect width="100%" height="100%" fill="{PALETTE["bg"]}"/>')
    def add(self, s): self.items.append(s)
    def text(self,x,y,t,size=18,weight='400',anchor='middle',fill=None,rot=None,style=''):
        fill=fill or PALETTE['ink']; tr=f' transform="rotate({rot} {x} {y})"' if rot else ''
        self.add(f'<text x="{x:.2f}" y="{y:.2f}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}"{tr} style="{style}">{esc(t)}</text>')
    def line(self,x1,y1,x2,y2,stroke=None,sw=1,opacity=1,dash=None):
        stroke=stroke or PALETTE['ink']; da=f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"{da}/>')
    def rect(self,x,y,w,h,fill='none',stroke=None,sw=1,rx=0,opacity=1):
        st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
        self.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" rx="{rx}" fill="{fill}" opacity="{opacity}"{st}/>')
    def circle(self,x,y,r,fill,stroke='white',sw=1,opacity=1):
        self.add(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{r:.2f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>')
    def path(self,d,fill='none',stroke=None,sw=2,opacity=1,dash=None):
        st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
        da=f' stroke-dasharray="{dash}"' if dash else ''
        self.add(f'<path d="{d}" fill="{fill}" opacity="{opacity}"{st}{da} stroke-linejoin="round" stroke-linecap="round"/>')
    def save(self,path):
        os.makedirs(os.path.dirname(path),exist_ok=True)
        with open(path,'w',encoding='utf-8') as f:
            f.write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}">\n')
            if self.defs: f.write('<defs>'+'\n'.join(self.defs)+'</defs>\n')
            f.write('\n'.join(self.items)); f.write('\n</svg>\n')

def plot_axes(svg, x,y,w,h, xmin,xmax,ymin,ymax, xticks, yticks, xlabel='', ylabel='', title=''):
    svg.rect(x,y,w,h,fill='white',stroke='#DDD7CB',sw=1.2,rx=12)
    def sx(v): return x + (v-xmin)/(xmax-xmin)*w
    def sy(v): return y+h - (v-ymin)/(ymax-ymin)*h
    for t in yticks:
        yy=sy(t); svg.line(x,yy,x+w,yy,PALETTE['grid'],1); svg.text(x-12,yy+5,t,14,anchor='end',fill=PALETTE['muted'])
    for t in xticks:
        xx=sx(t); svg.line(xx,y,xx,y+h,PALETTE['grid'],1,opacity=.65); svg.text(xx,y+h+24,t,14,fill=PALETTE['muted'])
    svg.line(x,y+h,x+w,y+h,PALETTE['ink'],1.5); svg.line(x,y,x,y+h,PALETTE['ink'],1.5)
    if xlabel: svg.text(x+w/2,y+h+50,xlabel,16,weight='700')
    if ylabel: svg.text(x-55,y+h/2,ylabel,16,weight='700',rot=-90)
    if title: svg.text(x+w/2,y-18,title,22,weight='700')
    return sx, sy

def line_series(svg, sx, sy, xs, ys, color, label=None, marker='circle', sw=3):
    pts=[(sx(a), sy(b)) for a,b in zip(xs,ys)]
    d='M '+' L '.join(f'{x:.2f},{y:.2f}' for x,y in pts)
    svg.path(d,stroke=color,sw=sw)
    for x,y in pts:
        if marker=='triangle':
            svg.path(f'M {x:.1f},{y-5:.1f} L {x-5:.1f},{y+5:.1f} L {x+5:.1f},{y+5:.1f} Z',fill=color,stroke='white',sw=1)
        else: svg.circle(x,y,4.2,color,sw=1)

def smooth_curve(start, final, peak, peak_day, n=21):
    vals=[]
    for d in range(n):
        if d <= peak_day:
            v=start + (peak-start)*(1-math.exp(-3*(d+0.15)/(peak_day+0.4)))
        else:
            v=peak + (final-peak)*(1-math.exp(-2.2*(d-peak_day)/(n-1-peak_day+0.1)))
        vals.append(round(v,3))
    vals[-1]=final
    return vals
