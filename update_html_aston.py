import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

aston_slide = """    <div class="slide">
      <main class="container car-section" data-price="Rp 7.500.000.000">
        <!-- Hero Section -->
        <header class="hero">
          <div class="sidebar">
            <div class="logo-box">
              <img src="https://upload.wikimedia.org/wikipedia/en/thumb/f/f5/Aston_Martin_logo.svg/1200px-Aston_Martin_logo.svg.png" alt="Aston Martin Logo" class="toyota-logo" style="width: 50px;">
              <h3 style="letter-spacing: 1px;">ASTON MARTIN</h3>
            </div>
            <div class="badge-red" style="background: #004225;">VANQUISH</div>
            <div class="badge-dark">V12</div>
            <div class="badge-text">2012-2018</div>
            <div class="flag" style="display:flex; flex-direction: column; border: none; background: #00247d; position: relative;">
               <!-- Fake union jack simplified -->
               <div style="width: 100%; height: 2px; background: white; position: absolute; top: 50%; transform: translateY(-50%);"></div>
               <div style="width: 2px; height: 100%; background: white; position: absolute; left: 50%; transform: translateX(-50%);"></div>
            </div>
          </div>

          <div class="hero-img-wrapper">
            <img src="images/Aston-Martin/hero_aston.png" alt="Aston Martin Vanquish Hero" class="hero-img" onerror="this.src='images/Toyota-supra/hero_supra.png'">
            
            <div class="hero-content">
              <h1 class="main-title" style="font-family: 'Montserrat', sans-serif; font-style: normal; letter-spacing: 5px; font-weight: 300;">
                <span class="small-toyota" style="letter-spacing: 20px;">ASTON MARTIN</span><br>
                VANQUISH
              </h1>
              <p class="subtitle">Power, Beauty, Soul <br> <span style="color: #004225;">GRAND TOURER</span></p>
            </div>
          </div>

          <div class="tagline">
            <div class="line"></div>
            <p>THE ULTIMATE GRAND TOURER.</p>
            <div class="line"></div>
          </div>
        </header>

        <!-- Specs Section -->
        <section class="specs-section">
          <div class="profile-img-container">
            <img src="images/Aston-Martin/profile_aston.png" alt="Vanquish Profile" class="profile-img" onerror="this.src='images/Toyota-supra/profile_supra.png'">
          </div>
          <div class="specs-list">
            <h2 class="section-title text-red" style="color: #004225;">SPECIFICATIONS</h2>
            <ul>
              <li><span class="icon">⚙️</span><div class="spec-text"><strong>ENGINE</strong><span>5.9L AM29 V12</span></div></li>
              <li><span class="icon">🐎</span><div class="spec-text"><strong>POWER</strong><span>568 hp @ 6,650 rpm</span></div></li>
              <li><span class="icon">🔄</span><div class="spec-text"><strong>TORQUE</strong><span>630 N·m @ 5,500 rpm</span></div></li>
              <li><span class="icon">🛣️</span><div class="spec-text"><strong>DRIVETRAIN</strong><span>RWD transaxle</span></div></li>
              <li><span class="icon">🕹️</span><div class="spec-text"><strong>TRANSMISSION</strong><span>8-Speed Touchtronic III</span></div></li>
              <li><span class="icon">⚖️</span><div class="spec-text"><strong>WEIGHT</strong><span>1,739 kg</span></div></li>
              <li><span class="icon">⏱️</span><div class="spec-text"><strong>0-100 km/h</strong><span>3.8 sec</span></div></li>
              <li><span class="icon">🚀</span><div class="spec-text"><strong>TOP SPEED</strong><span>324 km/h</span></div></li>
            </ul>
          </div>
        </section>

        <!-- Grid Section -->
        <section class="four-grid">
          <!-- Rear View -->
          <div class="grid-item">
            <h2 class="section-title text-red" style="color: #004225;">REAR VIEW</h2>
            <img src="images/Aston-Martin/rear_aston.png" alt="Vanquish Rear View" class="grid-img" onerror="this.src='images/Toyota-supra/rear_supra.png'">
          </div>
          <!-- Available Colors -->
          <div class="grid-item colors-section">
            <h2 class="section-title text-red" style="color: #004225;">AVAILABLE COLORS</h2>
            <ul class="color-list">
              <li><span class="color-dot" style="background: #004225;"></span> Appletree Green</li>
              <li><span class="color-dot" style="background: #1a1a1a;"></span> Onyx Black</li>
              <li><span class="color-dot" style="background: #d4af37;"></span> Sunburst Yellow</li>
              <li><span class="color-dot" style="background: #c0c0c0;"></span> Stratus White</li>
              <li><span class="color-dot" style="background: #738276;"></span> Quantum Silver</li>
              <li><span class="color-dot" style="background: #003366;"></span> Mariana Blue</li>
            </ul>
          </div>
          <!-- Engine -->
          <div class="grid-item">
            <h2 class="section-title text-red" style="color: #004225;">THE HEART – V12</h2>
            <img src="images/Aston-Martin/engine_aston.png" alt="Aston V12 Engine" class="grid-img" onerror="this.src='images/Toyota-supra/engine_supra.png'">
            <p class="desc-text">A naturally aspirated 5.9-liter V12 engine that delivers a symphony of sound and relentless power, the soul of the Vanquish.</p>
          </div>
          <!-- Interior -->
          <div class="grid-item">
            <h2 class="section-title text-red" style="color: #004225;">BESPOKE LUXURY</h2>
            <img src="images/Aston-Martin/interior_aston.png" alt="Vanquish Interior" class="grid-img" onerror="this.src='images/Toyota-supra/interior_supra.png'">
            <p class="desc-text">Bridge of Weir leather, carbon fiber fascia, and glass switches create an environment of unparalleled British luxury.</p>
          </div>
        </section>

        <!-- Footer Grid -->
        <section class="footer-grid">
          <div class="legend-box">
            <h2 class="section-title text-red" style="color: #004225;">BRITISH CRAFTSMANSHIP.</h2>
            <p class="desc-text">The Vanquish represents the pinnacle of Aston Martin design and engineering, combining aerospace-grade carbon fiber with traditional hand-built luxury.</p>
            <div class="logos-bottom">
              <h1 class="supra-logo-text" style="font-family: 'Montserrat', sans-serif; font-weight: 300;">ASTON MARTIN</h1>
            </div>
          </div>
          <div class="dimensions-box">
            <h2 class="section-title text-red" style="color: #004225;">DIMENSIONS</h2>
            <div class="dim-graphics-container">
               <img src="images/Aston-Martin/aston_blueprint.png" alt="Vanquish Dimensions Blueprint" class="blueprint-img" onerror="this.src='images/Toyota-supra/supra_blueprint.png'">
               <div class="dim-text-overlay">
                 <div class="dim-text"><span style="color: #004225;">Width:</span> 1,912 mm</div>
                 <div class="dim-text"><span style="color: #004225;">Height:</span> 1,294 mm</div>
                 <div class="dim-text"><span style="color: #004225;">Wheelbase:</span> 2,740 mm</div>
                 <div class="dim-text"><span style="color: #004225;">Length:</span> 4,728 mm</div>
               </div>
            </div>
          </div>
        </section>
      </main>
    </div>
"""

content = content.replace("    </div>\n  </div>\n</div>\n\n  <script>", "    </div>\n" + aston_slide + "  </div>\n</div>\n\n  <script>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
