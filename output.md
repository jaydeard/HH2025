
### Problem HH-RAYTRACING-0001
**Wavefront Reconstruction Using Ray-Tracing**

*Insight*: Ray-tracing helps to mathematically describe how interference patterns encode spatial information, allowing virtual and real images to be reconstructed accurately.

**Question**: A point object is placed at z = -500 mm along the optical axis in a Gabor holographic setup. The reference beam is a plane wave traveling parallel to the z-axis. Calculate the spatial frequency of the interference fringes at a point 50 mm above the optical axis on the hologram surface, given a He-Ne laser with a wavelength of 633 nm.


<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-RAYTRACING-0001.png" alt="Alt Text" width="200" height="133">

---

### Solution for Problem HH-RAYTRACING-0001
<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-RAYTRACING-0001s.png" alt="Alt Text" width="200" height="133">

**Answer**: f ≈ 157.2 cycles/mm

**Steps:**

1. **Step 1: Set up the spatial frequency equation**
2. The spatial frequency is given by: $$f = \frac{\sin(\theta_{obj}) - \sin(\theta_{ref})}{\lambda}$$.
3. **Step 2: Calculate object beam angle**
4. Using trigonometry: $$\theta_{obj} = \arctan(\frac{50}{500}) = 0.0997$$.
5. **Step 3: Substitute values into the formula**
6. $$f = \frac{0.1}{633 \times 10^{-6}} = 157 \, \text{cycles/mm}$$.

---

### Problem HH-RAYTRACING-0002
**Spatial Frequency in Wavefront Reconstruction**

*Insight*: The spatial frequency of interference fringes depends on the angles of object and reference beams relative to the hologram surface.

**Question**: In a holographic setup, we place the film on the plane z = 0. An object is placed at the point z = -600 mm and y = -300 mm (y = 0 is the optical axis). The reference beam travels parallel to the z-axis. Using a laser with a wavelength of 532 nm, determine the spatial frequency of the interference fringes at a point y = 30 mm on the film surface (z = 0).


<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-RAYTRACING-0002.png" alt="Alt Text" width="200" height="133">

---

### Solution for Problem HH-RAYTRACING-0002
<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-RAYTRACING-0002s.png" alt="Alt Text" width="200" height="133">

**Answer**: f ≈ 905.86 cycles/mm

**Steps:**

1. **Step 1: Write the spatial frequency formula**
2. $$f = \frac{\sin(\theta_{obj}) - \sin(\theta_{ref})}{\lambda}$$.
3. **Step 2: Determine the angle of the object beam**
4. Using trigonometry: $$\theta_{obj} = \arctan(\frac{330}{600}) = 0.5028 rad$$.
5. **Step 3: Substitute the given values**
6. $$f = \frac{0.05 - 0}{532 \times 10^{-6}}$$.
7. **Step 4: Perform the calculation**
8. $$f = \frac{0.5028}{532 \times 10^{-6}} = 905.86 \, \text{cycles/mm}$$.

---

### Problem HH-RAYTRACING-0003
**Numerical Ray-Tracing: Image Position and Aberration**

*Insight*: Numerical ray-tracing helps accurately predict image positions and identify aberrations caused by beam geometry and recording parameters.

**Question**: In a holographic imaging system, an object point is located 400 mm below the optical axis, and a reference beam is incident at an angle of 5° with respect to the optical axis. The recording wavelength is 633 nm, and the hologram is located 800 mm away from the object plane. Using numerical ray-tracing, determine the position of the reconstructed image along the z-axis.


<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-RAYTRACING-0003.png" alt="Alt Text" width="200" height="133">

---

### Solution for Problem HH-RAYTRACING-0003
<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-RAYTRACING-0003s.png" alt="Alt Text" width="200" height="133">

**Answer**: The reconstructed image is located at approximately z = 823.6 mm.

**Steps:**

1. **Step 1: Write the image position formula from ray-tracing principles**
2. $$z' = \frac{z}{1 - \frac{z}{R}}$$, where R is the effective radius of curvature due to the reference beam.
3. **Step 2: Approximate the radius of curvature (R)**
4. Using the angle: $$R = \frac{z}{\sin(\theta)}$$.
5. Substitute the values: $$R = \frac{800}{\sin(5^\circ)}$$.
6. **Step 3: Calculate sin(5°)**
7. $$\sin(5^\circ) ≈ 0.0872$$.
8. $$R = \frac{800}{0.0872} ≈ 9170 \text{ mm}$$.
9. **Step 4: Substitute into the image position formula**
10. $$z' = \frac{800}{1 - \frac{800}{9170}}$$.
11. **Step 5: Simplify the fraction**
12. $$1 - \frac{800}{9170} ≈ 0.9127$$.
13. $$z' = \frac{800}{0.9127} ≈ 876.4 \text{ mm}$$.
14. **Step 6: Interpret the result**
15. The reconstructed image appears at approximately z = 823.6 mm along the optical axis.
16. **Additional Context / Clarification:**
17. The slight discrepancy in image position is caused by the reference beam's finite angle, introducing a small aberation. Numerical ray-tracing provides a more accurate prediction of image location compared to simplified geometrical approximations.

---

### Problem HH-RAYTRACING-0003
**Numerical Ray-Tracing: Image Position and Aberration**

*Insight*: Numerical ray-tracing helps accurately predict image positions and identify aberrations caused by beam geometry and recording parameters.

**Question**: In a holographic imaging system, an object point is located 400 mm below the optical axis, and a reference beam is incident at an angle of 5° with respect to the optical axis. The recording wavelength is 633 nm, and the hologram is located 800 mm away from the object plane. Using numerical ray-tracing, determine the position of the reconstructed image along the z-axis.


<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-RAYTRACING-0003.png" alt="Alt Text" width="200" height="133">

---

### Solution for Problem HH-RAYTRACING-0003
<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-RAYTRACING-0003s.png" alt="Alt Text" width="200" height="133">

**Answer**: The reconstructed image is located at approximately z = 823.6 mm.

**Steps:**

1. **Step 1: Write the image position formula from ray-tracing principles**
2. $$z' = \frac{z}{1 - \frac{z}{R}}$$, where R is the effective radius of curvature due to the reference beam.
3. **Step 2: Approximate the radius of curvature (R)**
4. Using the angle: $$R = \frac{z}{\sin(\theta)}$$.
5. Substitute the values: $$R = \frac{800}{\sin(5^\circ)}$$.
6. **Step 3: Calculate sin(5°)**
7. $$\sin(5^\circ) ≈ 0.0872$$.
8. $$R = \frac{800}{0.0872} ≈ 9170 \text{ mm}$$.
9. **Step 4: Substitute into the image position formula**
10. $$z' = \frac{800}{1 - \frac{800}{9170}}$$.
11. **Step 5: Simplify the fraction**
12. $$1 - \frac{800}{9170} ≈ 0.9127$$.
13. $$z' = \frac{800}{0.9127} ≈ 876.4 \text{ mm}$$.
14. **Step 6: Interpret the result**
15. The reconstructed image appears at approximately z = 823.6 mm along the optical axis.
16. **Additional Context / Clarification:**
17. The slight discrepancy in image position is caused by the reference beam's finite angle, introducing a small aberation. Numerical ray-tracing provides a more accurate prediction of image location compared to simplified geometrical approximations.

---

### Problem HH-RAYTRACING-0004
**Numerical Ray-Tracing: Image Shift Due to Reference Beam Angle**

*Insight*: The angle of the reference beam introduces shifts in the reconstructed image position, which can be quantified through numerical ray-tracing.

**Question**: In a holographic setup, an object is positioned 500 mm below the optical axis, and the reference beam makes an angle of 7° with the z-axis. The hologram is located 1000 mm from the object plane, and the laser wavelength is 532 nm. Using numerical ray-tracing, determine the lateral image shift caused by the reference beam angle.


<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-RAYTRACING-0004.png" alt="Alt Text" width="200" height="133">

---

### Solution for Problem HH-RAYTRACING-0004
<img src="https://s3.us-east-2.amazonaws.com/hh.images/FIG-RAYTRACING-0004s.png" alt="Alt Text" width="200" height="133">

**Answer**: The lateral image shift is approximately 122.1 mm.

**Steps:**

1. **Step 1: Write the lateral shift formula**
2. $$\Delta x = z \tan(\theta)$$, where $$z$$ is the object-to-hologram distance and $$\theta$$ is the reference beam angle.
3. **Step 2: Substitute the given values**
4. $$z = 1000 \text{ mm}$$, $$\theta = 7^\circ$$.
5. $$\Delta x = 1000 \cdot \tan(7^\circ)$$.
6. **Step 3: Calculate $$\tan(7^\circ)$$**
7. $$\tan(7^\circ) ≈ 0.1221$$.
8. **Step 4: Perform the multiplication**
9. $$\Delta x = 1000 \cdot 0.1221 = 122.1 \text{ mm}$$.
10. **Step 5: Final Answer**
11. The lateral image shift caused by the reference beam angle is approximately 122.1 mm.
12. **Additional Context / Clarification:**
13. The angle of the reference beam introduces a predictable lateral shift in the reconstructed image. This effect becomes more significant as the reference beam angle increases, requiring precise numerical ray-tracing for accurate corrections.

---
