
### Problem HH-PHASE-0001
**Phase Footprint of a Point Source on a Plane**
**Question**: Given a point source of λ = 633 nm wavelength at the coordinate (x0, z0) = (0, -1000 mm), what is the phase footprint at the plane z=0? You may assume that the constant phase term (on-axis phase) is zero. Express your final answer in degrees as a function of (x² + y²).


---

### Solution for Problem HH-PHASE-0001
**Answer**: φ(x, y) ≈ 284.4 (x² + y²) degrees.

**Steps:**

1. 1. Convert the wavelength to millimeters: λ = 633 nm = 0.000633 mm.
2. 2. The (angular) phase constant in degrees per mm is k_deg = 360° / λ. Numerically, k_deg ≈ 360° / 0.000633 mm ≈ 568,830 deg/mm.
3. 3. The path length from the source to a point (x, y, 0) is L = √(1000² + r²), where r² = x² + y². The on-axis path is 1000 mm, so the extra distance is ΔL = L - 1000.
4. 4. For r ≪ 1000 mm, use the binomial expansion: √(1000² + r²) ≈ 1000 + r² / (2 × 1000). Hence, ΔL ≈ r² / (2 × 1000).
5. 5. The phase (in degrees) is φ(r) = k_deg × ΔL = (568,830 deg/mm) × (r² / (2 × 1000)).
6. 6. Combine constants: 568,830 / (2 × 1000) ≈ 284.4, so φ(r) ≈ 284.4 (x² + y²).
7. 7. The phase footprint (ignoring the constant term) is therefore φ(x, y) = 284.4 (x² + y²) degrees.

---
