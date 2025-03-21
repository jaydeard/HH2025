
### Problem HH-INTERFERENCE-0010
**Fringe Spacing in Interference Patterns**
*Insight*: Fringe spacing depends on the angle between the object and reference beams and the wavelength of light used.

**Question**: A plane wave reference beam intersects an object beam at an angle of 30° on a holographic plate. The laser wavelength is 532 nm. Calculate the fringe spacing.


<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-INTERFERENCE-0010.png" alt="Alt Text" width="200" height="133">

---

### Solution for Problem HH-INTERFERENCE-0010
<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-INTERFERENCE-0010s.png" alt="Alt Text" width="200" height="133">

**Answer**: d ≈ 1.06 µm

**Steps:**

1. The fringe spacing formula is: $$d = \frac{\lambda}{2 \sin(\theta/2)}$$.
2. Substitute the given values: $$\lambda = 532 \times 10^{-9} \text{ m}$$, $$\theta = 30°$$.
3. Calculate: $$\sin(15°) = 0.2588$$.
4. Evaluate the denominator: $$2 \cdot 0.2588 = 0.5176$$.
5. Divide: $$d = \frac{532 \times 10^{-9}}{0.5176}$$.
6. Simplify: $$d ≈ 1.06 \times 10^{-6} \text{ m}$$.
7. Convert to micrometers: $$d ≈ 1.06 \text{ µm}$$.
8. Conclusion: The fringe spacing is approximately 1.06 µm.

---

### Problem HH-INTERFERENCE-0040
**Interference of Light Waves: Intensity at Different Phases**
*Insight*: The total intensity of overlapping coherent waves depends on the phase difference, and the combined intensity can be calculated using an interference formula.

**Question**: Let two coherent (i.e., same frequency, with a constant phase difference) light waves overlap, one with an intensity of 10 milliwatts per square centimeter, and the other with an intensity of 20 milliwatts per square centimeter. What is the intensity of the combined wave field at a location chosen such that the waves arrive:

a) In phase (crests meet crests, etc.)
b) Out of phase (crests meet troughs)
c) Ninety degrees out of phase (halfway in between)?

*Hint:* Use the formula for total intensity:
$$I_{total} = I_1 + I_2 + 2 \sqrt{I_1 I_2} \cos(\phi)$$


<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-INTERFERENCE-0040.png" alt="Alt Text" width="200" height="133">

---

### Solution for Problem HH-INTERFERENCE-0040
<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-INTERFERENCE-0040s.png" alt="Alt Text" width="200" height="133">

**Answer**: a) 58.3 mW/cm², b) 1.72 mW/cm², c) 30 mW/cm²

**Steps:**

1. Use the formula for total intensity: $$I_{total} = I_1 + I_2 + 2 \sqrt{I_1 I_2} \cos(\phi)$$.
2. Substitute the given values: $$I_1 = 10$$, $$I_2 = 20$$, and calculate $$\sqrt{200} = 14.14$$.
3. For in-phase (0°): $$I_{total} = 10 + 20 + 2(14.14)(1) = 58.3 \text{ mW/cm}^2$$.
4. For out-of-phase (180°): $$I_{total} = 10 + 20 + 2(14.14)(-1) = 1.72 \text{ mW/cm}^2$$.
5. For 90° out of phase: $$I_{total} = 10 + 20 + 2(14.14)(0) = 30 \text{ mW/cm}^2$$.

---

### Problem HH-INTERFERENCE-0003
**Visibility of Interference Patterns in Holography**
*Insight*: The visibility of interference patterns depends on the V-parameter, which compares the intensities of the reference and object waves.

**Question**: The book claims that a reference wave 1/40000ths of the power of an object wave can interfere to form visible patterns on a hologram. Given that a V-parameter, V=0.01 is the threshold of human vision, is it true that such a difference in intensity can still cause a visible interference pattern?


<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-INTERFERENCE-0003.png" alt="Alt Text" width="200" height="133">

---

### Solution for Problem HH-INTERFERENCE-0003
<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-INTERFERENCE-0003s.png" alt="Alt Text" width="200" height="133">

**Answer**: V = 0.0099975, true

**Steps:**

1. Use the visibility formula: $$V = \frac{2\sqrt{I_1 I_2}}{I_1 + I_2}$$.
2. Substitute the given intensity ratio: $$I_1 = 40000 I_2$$.
3. Simplify: $$V = \frac{2 \sqrt{40000}}{40000 + 1}$$.
4. Evaluate: $$= \frac{2 (200)}{40001} = 0.0099975$$.
5. Compare with the threshold value (0.01): since 0.0099975 is approximately equal to 0.01, the pattern is visible.
6. Conclusion: The interference pattern is still visible despite the intensity difference.

---

### Problem HH-MICHELSON-0001
**Michelson Interferometer: Fringe Spacing and Source Separation**
*Insight*: Fringe spacing in an interferometer depends on the wavelength of light, the distance to the screen, and the angular separation of the point sources.

**Question**: In a Michelson Interferometer, two dark fringes are spaced 1 inch apart (measured center-to-center). These fringes are observed on a screen placed 60 cm away from the lens. If the wavelength of the laser used is 632 nm, determine the separation between the two point sources (formed by the He-Ne laser images). Use the relationship:
$$\sin(\theta) - \sin(-\theta) = \frac{\lambda}{d}$$
and approximate $$\tan(\theta) \approx \sin(\theta)$$ for the easy solution. Verify whether the results from the exact and approximate methods are nearly identical.


<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-MICHELSON-0001.png" alt="Alt Text" width="200" height="133">

---

### Solution for Problem HH-MICHELSON-0001
<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-MICHELSON-0001s.png" alt="Alt Text" width="200" height="133">

**Answer**: d = 15 μm

**Steps:**

1. **Hard Solution:**
2. 1. Use the relation: $$\sin(\theta) - \sin(-\theta) = \frac{\lambda}{d}$$ which simplifies to $$2\sin(\theta) = \frac{\lambda}{d}$$.
3. 2. Express the angle in terms of fringe spacing and screen distance: $$\tan(\theta) = \frac{d}{2L}$$.
4. 3. Substitute into the sine expression: $$2\sin(\arctan(\frac{d}{2L})) = \frac{\lambda}{d}$$.
5. 4. Solve numerically: $$\theta = \arctan(\frac{25.4 \times 10^{-3}}{2 \times 60 \times 10^{-2}})$$.
6. 5. Substitute back and solve for $$d$$.
7. 6. Result: $$d = 15 \mu m$$.
8. **Easy Solution:**
9. 1. Approximate $$\tan(\theta) \approx \sin(\theta)$$ for small angles.
10. 2. Substitute into the formula: $$d \approx \frac{\lambda L}{\Lambda}$$, where $$\Lambda$$ is the fringe spacing (25.4 mm).
11. 3. Substitute the values: $$d = \frac{632 \times 10^{-9} \cdot 60 \times 10^{-2}}{25.4 \times 10^{-3}}$$.
12. 4. Result: $$d = 15 \mu m$$.
13. 5. Verify that both methods yield nearly identical results.

---

### Problem HH-COHERENCE-0001
**Coherence Length and Spectral Width in Interferometry**
*Insight*: The coherence length determines the maximum path difference for visible interference patterns, while the spectral width depends on the wavelength and coherence length.

**Question**: A student installs a 550 nm laser in a classic Michelson interferometer setup. By moving one of the mirrors, he manipulates the optical path difference of the beam. He moves the mirror until the interference lines disappear. At this distance, the difference between the beams is 1 m.

**a)** What is the coherent length of the laser?
**b)** What is the spectral width of the laser?

**Hint:** Use the formulas $$d \approx 2\Delta$$ for coherence length and $$d \approx \frac{\lambda_0^2}{\Delta \lambda}$$ for spectral width.


<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-COHERENCE-0001.png" alt="Alt Text" width="200" height="133">

---

### Solution for Problem HH-COHERENCE-0001
<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-COHERENCE-0001s.png" alt="Alt Text" width="200" height="133">

**Answer**: a) d ≈ 2 m, b) Δλ ≈ 151.25 fm

**Steps:**

1. **Part (a): Coherence Length**
2. 1. Use the formula: $$d \approx 2 \Delta$$.
3. 2. Substitute the given path difference: $$\Delta = 1 \text{ m}$$.
4. 3. Calculate: $$d = 2 \cdot 1 = 2 \text{ m}$$.
5. 4. The coherence length of the laser is approximately 2 m.
6. **Additional Context / Clarification:**
7. Why $$d ≈ 2 Δ$$: In a Michelson interferometer, if you move one mirror by a distance $$Δ$$, the round-trip OPD (Optical Path Difference) changes by $$2 Δ$$. If interference vanishes for $$Δ = 1 \text{ m}$$, the total path difference is $$2 \text{ m}$$. That value is then interpreted as the laser’s coherence length.
8. **Part (b): Spectral Width**
9. 1. Use the formula: $$d \approx \frac{\lambda_0^2}{\Delta \lambda}$$.
10. 2. Rearrange for $$\Delta \lambda$$: $$\Delta \lambda = \frac{\lambda_0^2}{d}$$.
11. 3. Substitute the given values: $$\lambda_0 = 550 \times 10^{-9} \text{ m}$$, $$d = 2 \text{ m}$$.
12. 4. Calculate: $$\Delta \lambda = \frac{(550 \times 10^{-9})^2}{2} = 151.25 \text{ fm}$$.
13. 5. The spectral width of the laser is approximately 151.25 fm.
14. **Additional Context / Clarification:**
15. Why $$d ≈ \frac{\lambda_0^2}{\Delta \lambda}$$: This formula represents a simplified relationship between the coherence length $$d$$ and the spectral width $$\Delta \lambda$$ for a single-mode or narrowband source around a central wavelength $$\lambda_0$$. While real lasers can exhibit more complex spectral line shapes, this approximation provides a good estimate for the order of magnitude of $$\Delta \lambda$$ in standard textbook problems.

---
