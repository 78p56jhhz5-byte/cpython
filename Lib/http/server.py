<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dell | Orbital Creative Portfolio</title>
    <meta name="description" content="Personal interactive portfolio of Dell, engineered with a scroll-rotatable orbital mind map layout.">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
    <!-- FontAwesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Canvas for particle stream network -->
    <canvas id="ambient-canvas"></canvas>
    <!-- UI Overlay Elements -->
    <div class="cyber-scanlines"></div>
    <!-- App Header -->
    <header class="app-header">
        <div class="logo">
            <i class="fa-solid fa-satellite-dish pulse-glow"></i>
            <span>DELL_PORTAL</span>
        </div>
        <div class="controls-panel">
            <span class="ctrl-label">NODE FILTERS:</span>
            <button class="filter-btn active" data-category="all">All</button>
            <button class="filter-btn" data-category="identity">Identity</button>
            <button class="filter-btn" data-category="creations">Creations</button>
            <button class="filter-btn" data-category="network">Network</button>
        </div>
        <div class="header-actions">
            <button class="cyber-btn" id="grid-snap-btn" title="Snap to Linear Grid">
                <i class="fa-solid fa-table-cells-large"></i>
                <span>GRID SNAP</span>
            </button>
            <button class="cyber-btn secondary" id="overdrive-toggle">
                <i class="fa-solid fa-radiation"></i>
                <span>OVERDRIVE</span>
            </button>
        </div>
    </header>
    <!-- Main Panoramic Workspace -->
    <div class="workspace">
        <section class="viewport" id="map-viewport">
            <!-- SVG paths layer for connection lines -->
            <svg class="line-overlay" id="svg-connections"></svg>
            <!-- Draggable Map Board -->
            <div class="map-board" id="map-board">
                <!-- Center Core Profile Node -->
                <div class="core-profile" id="center-core">
                    <div class="avatar-box">
                        <img src="avatar.jpg" alt="Dell Avatar" onerror="this.src='https://placehold.co/120x120/0f172a/00f0ff?text=DELL'">
                    </div>
                    <div class="core-title">
                        <span class="core-name">DELL</span>
                        <span class="core-sub">COGNITIVE DEV</span>
                    </div>
                    <!-- Concentric Orbit Guides -->
                    <div class="orbit-guide ring-1"></div>
                    <div class="orbit-guide ring-2"></div>
                    <div class="orbit-guide ring-3"></div>
                </div>
                <!-- Satellites will be injected dynamically by JS -->
            </div>
            <!-- Dashboard HUD info -->
            <div class="system-hud">
                <div class="hud-item">
                    <span class="lbl">LATENCY:</span>
                    <span class="val" style="color: var(--neon-cyan)">0.04 ms</span>
                </div>
                <div class="hud-item">
                    <span class="lbl">COGNITIVE LEVEL:</span>
                    <span class="val" style="color: var(--neon-purple)">SYNCHRONIZED</span>
                </div>
            </div>
            <!-- Dynamic Guide overlay -->
            <div class="navigation-tooltip">
                <i class="fa-solid fa-circle-info"></i> Drag backdrop to pan. Scroll mouse wheel to rotate orbits. Click nodes to inspect.
            </div>
        </section>
        <!-- Right sliding details drawer -->
        <aside class="details-drawer" id="side-drawer">
            <div class="drawer-header">
                <div class="drawer-badge" id="drawer-tag">PORTAL NODE</div>
                <button class="close-btn" id="close-drawer"><i class="fa-solid fa-xmark"></i></button>
            </div>
            <div class="drawer-scroll-container" id="drawer-body-container">
                <div class="drawer-placeholder">
                    <i class="fa-solid fa-circle-nodes"></i>
                    <h3>Portal Node Scanner</h3>
                    <p>Select any floating satellite node on the orbital canvas map to connect and read diagnostic data.</p>
                </div>
            </div>
        </aside>
    </div>
    <script src="app.js"></script>
</body>
</html>
