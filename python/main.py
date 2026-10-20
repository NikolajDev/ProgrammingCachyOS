from manim import *

class VelkyPrehladOborov(Scene):
    def construct(self):
        # Úvodný nadpis
        title = Text("Definičný obor funkcie: Kompletný sprievodca", font_size=28, color=BLUE)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # --- ČASŤ 1: Všeobecné pravidlá ---
        rule_title = Text("1. Všeobecné pravidlá", font_size=22, color=YELLOW).to_edge(LEFT).shift(UP * 2.2)
        r1 = MathTex(r"\text{- Zlomky: } \text{menovateľ} \neq 0", font_size=18)
        r2 = MathTex(r"\text{- Párne odmocniny: } \text{pod odmocninou} \ge 0", font_size=18)
        r3 = MathTex(r"\text{- Logaritmy: } \text{argument} > 0", font_size=18)
        r4 = MathTex(r"\text{- Arcsin / Arccos: } -1 \le \text{argument} \le 1", font_size=18)
        r5 = MathTex(r"\text{- Tangens: } x \neq \frac{\pi}{2} + k\pi, \quad \text{- Kotangens: } x \neq k\pi", font_size=18)

        rules_group = VGroup(r1, r2, r3, r4, r5).arrange(DOWN, aligned_edge=LEFT, buff=0.15).next_to(rule_title, DOWN, aligned_edge=LEFT)

        self.play(Write(rule_title), FadeIn(rules_group, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(rule_title), FadeOut(rules_group))

        # --- ČASŤ 2: Príklady a) až d) ---
        ex_title1 = Text("2. Príklady a) – d)", font_size=22, color=YELLOW).to_edge(LEFT).shift(UP * 2.3)
        e1 = MathTex(r"\text{a) } f(x) = \sqrt[3]{\ln \frac{5x-x^2}{4}} \implies D(f) = (0, 5)", font_size=18)
        e2 = MathTex(r"\text{b) } f(x) = \arccos \frac{(x+3)^2}{9} \implies D(f) = [-6, 0]", font_size=18)
        e3 = MathTex(r"\text{c) } y = \sqrt{\ln x} \implies D(f) = [1, \infty)", font_size=18)
        e4 = MathTex(r"\text{d) } f(x) = \operatorname{tg}\left(x - \frac{\pi}{4}\right) \implies x \neq \frac{3\pi}{4} + k\pi", font_size=18)

        ex_group1 = VGroup(e1, e2, e3, e4).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(ex_title1, DOWN, aligned_edge=LEFT)

        self.play(Write(ex_title1), FadeIn(ex_group1, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(ex_title1), FadeOut(ex_group1))

        # --- ČASŤ 3: Príklady e) až h) ---
        ex_title2 = Text("3. Príklady e) – h)", font_size=22, color=YELLOW).to_edge(LEFT).shift(UP * 2.3)
        e5 = MathTex(r"\text{e) } f(x) = \arcsin \frac{x-1}{x} \implies D(f) = \left[\frac{1}{2}, \infty\right)", font_size=18)
        e6 = MathTex(r"\text{f) } y = \ln\left(\ln \frac{x+2}{x-1}\right) \implies D(f) = (1, \infty)", font_size=18)
        e7 = MathTex(r"\text{g) } f(x) = \sqrt{\frac{x^2+x-2}{x+3}} \implies D(f) = (-3, -2] \cup [1, \infty)", font_size=18)
        e8 = MathTex(r"\text{h) } y = \log_3 \frac{x-6}{x} + \arcsin \frac{x+1}{6} \implies D(f) = [-7, 0) \cup (6, 5]", font_size=18)

        ex_group2 = VGroup(e5, e6, e7, e8).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(ex_title2, DOWN, aligned_edge=LEFT)

        self.play(Write(ex_title2), FadeIn(ex_group2, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(ex_title2), FadeOut(ex_group2))

        # --- ČASŤ 4: Príklady i) až l) ---
        ex_title3 = Text("4. Príklady i) – l)", font_size=22, color=YELLOW).to_edge(LEFT).shift(UP * 2.3)
        e9 = MathTex(r"\text{i) } y = \operatorname{cotg}\left(2x - \frac{\pi}{3}\right) + \sqrt{4-x^2} \implies D(f) = [-2, 2] \setminus \{\dots\}", font_size=18)
        e10 = MathTex(r"\text{j) } y = \arccos \frac{x+3}{2} + \sqrt{x+2} \implies D(f) = [-2, -1]", font_size=18)
        e11 = MathTex(r"\text{k) } y = \sqrt{x^2-4x+3} - \frac{1}{\sqrt[3]{4-x^2}} \implies D(f) = (-\infty, 1] \cup [3, \infty)", font_size=18)
        e12 = MathTex(r"\text{l) } y = \operatorname{tg} \frac{2x-\pi}{6} \implies x \neq 2\pi + 3k\pi", font_size=18)

        ex_group3 = VGroup(e9, e10, e11, e12).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(ex_title3, DOWN, aligned_edge=LEFT)

        self.play(Write(ex_title3), FadeIn(ex_group3, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(ex_title3), FadeOut(ex_group3))

        # --- ČASŤ 5: Príklady m) až p) ---
        ex_title4 = Text("5. Príklady m) – p)", font_size=22, color=YELLOW).to_edge(LEFT).shift(UP * 2.3)
        e13 = MathTex(r"\text{m) } y = \frac{\sin 2x}{1 - \cos 3x} \implies x \neq \frac{2k\pi}{3}", font_size=18)
        e14 = MathTex(r"\text{n) } y = \sqrt{1 - 2\sin 2x} \implies D(f) = \text{intervaly s arkussínusom}", font_size=18)
        e15 = MathTex(r"\text{o) } y = \operatorname{arctg} \frac{x+2}{x+3} \implies D(f) = \mathbb{R} \setminus \{-3\}", font_size=18)
        e16 = MathTex(r"\text{p) } y = \ln \sin\left(x + \frac{\pi}{4}\right) \implies \text{intervaly kde } \sin > 0", font_size=18)

        ex_group4 = VGroup(e13, e14, e15, e16).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(ex_title4, DOWN, aligned_edge=LEFT)

        self.play(Write(ex_title4), FadeIn(ex_group4, shift=DOWN))
        self.wait(3)
        self.play(FadeOut(ex_title4), FadeOut(ex_group4))

        # Záverečný odkaz
        outro = Text("Veľa šťastia so skúškami na VŠB-TUO!", font_size=26, color=PINK)
        self.play(Write(outro))
        self.wait(2)