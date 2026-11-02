with open('app/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Enhance lamp click handling so it is 100% foolproof
old_listeners = """  // Canvas interaction listeners
  canvas.addEventListener('pointerenter', function () { hasHover = true; });
  canvas.addEventListener('pointerleave', function () { if (!isDragging) hasHover = false; });

  canvas.addEventListener('pointerdown', function (e) {
    e.preventDefault();
    isDragging = true;
    hasHover = true;
    var c = getCanvasCoords(e);
    mouseX = c.x;
    mouseY = c.y;
    startPointerX = c.rawX;
    startPointerY = c.rawY;
    canvas.setPointerCapture(e.pointerId);
  });

  canvas.addEventListener('pointermove', function (e) {
    if (isDragging || hasHover) {
      var c = getCanvasCoords(e);
      mouseX = c.x;
      mouseY = c.y;
    }
  });

  canvas.addEventListener('pointerup', function (e) {
    if (isDragging) {
      isDragging = false;
      hasHover = false;
      try { canvas.releasePointerCapture(e.pointerId); } catch (err) {}
      
      var c = getCanvasCoords(e);
      var moveDist = Math.hypot(c.rawX - startPointerX, c.rawY - startPointerY);
      
      // If user tapped/clicked or dragged slightly (< 12px) -> trigger clean J-pull toggle!
      if (moveDist < 12) {
        triggerJPull();
      } else {
        // If dragged significantly downwards (> 18px)
        var tip = nodes[numNodes - 1];
        var restTipY = rootY + (numNodes - 1) * segLen;
        if (tip.y - restTipY > 18) {
          toggleLight();
          whipEnergy = 14;
        }
      }
    }
  });

  canvas.addEventListener('pointercancel', function (e) {
    isDragging = false;
    hasHover = false;
  });

  // Bulb element click directly triggers J-pull toggle
  if (bulbEl) {
    bulbEl.addEventListener('click', function (e) {
      e.stopPropagation();
      triggerJPull();
    });
  }"""

new_listeners = """  // Canvas & lamp interaction listeners
  canvas.addEventListener('pointerenter', function () { hasHover = true; });
  canvas.addEventListener('pointerleave', function () { if (!isDragging) hasHover = false; });

  var didDragMove = false;

  canvas.addEventListener('pointerdown', function (e) {
    isDragging = true;
    hasHover = true;
    didDragMove = false;
    var c = getCanvasCoords(e);
    mouseX = c.x;
    mouseY = c.y;
    startPointerX = c.rawX;
    startPointerY = c.rawY;
    try { canvas.setPointerCapture(e.pointerId); } catch (err) {}
  });

  canvas.addEventListener('pointermove', function (e) {
    if (isDragging || hasHover) {
      var c = getCanvasCoords(e);
      mouseX = c.x;
      mouseY = c.y;
      if (isDragging && Math.hypot(c.rawX - startPointerX, c.rawY - startPointerY) > 8) {
        didDragMove = true;
      }
    }
  });

  canvas.addEventListener('pointerup', function (e) {
    if (isDragging) {
      isDragging = false;
      hasHover = false;
      try { canvas.releasePointerCapture(e.pointerId); } catch (err) {}
      
      var c = getCanvasCoords(e);
      var moveDist = Math.hypot(c.rawX - startPointerX, c.rawY - startPointerY);
      
      if (!didDragMove || moveDist < 12) {
        triggerJPull();
      } else {
        var tip = nodes[numNodes - 1];
        var restTipY = rootY + (numNodes - 1) * segLen;
        if (tip.y - restTipY > 16) {
          toggleLight();
          whipEnergy = 15;
        }
      }
    }
  });

  canvas.addEventListener('pointercancel', function () {
    isDragging = false;
    hasHover = false;
  });

  // Direct click / tap fallbacks on canvas, bulb, and fixture
  canvas.addEventListener('click', function (e) {
    e.stopPropagation();
    if (!didDragMove) {
      triggerJPull();
    }
  });

  if (bulbEl) {
    bulbEl.addEventListener('click', function (e) {
      e.stopPropagation();
      triggerJPull();
    });
  }

  if (lampWrapper) {
    lampWrapper.addEventListener('click', function (e) {
      if (e.target !== canvas && e.target !== bulbEl) {
        triggerJPull();
      }
    });
  }"""

c = c.replace(old_listeners, new_listeners)

with open('app/index.html', 'w', encoding='utf-8') as f:
    f.write(c)

with open('marcus-bennet-pull-light.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Updated listeners and wrote both app/index.html and marcus-bennet-pull-light.html successfully!")

