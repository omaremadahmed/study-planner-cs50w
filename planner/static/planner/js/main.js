(() => {
  let time = 1500;
  let interval = null;

  function getTimerEl() {
    return document.getElementById("timer");
  }

  function renderTime() {
    const timerEl = getTimerEl();
    if (!timerEl) return;
    const minutes = Math.floor(time / 60);
    const seconds = time % 60;
    timerEl.innerText = `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
  }

  function startTimer() {
    if (!getTimerEl()) return; // only run on Pomodoro page
    if (interval) return; // prevent double-start

    interval = setInterval(() => {
      renderTime();
      time--;

      if (time < 0) {
        clearInterval(interval);
        interval = null;
        alert("Session Finished!");
      }
    }, 1000);
  }

  function resetTimer() {
    if (!getTimerEl()) return;
    if (interval) {
      clearInterval(interval);
      interval = null;
    }
    time = 1500;
    renderTime();
  }

  // Expose for inline onclick handlers in templates
  window.startTimer = startTimer;
  window.resetTimer = resetTimer;

  // If the page contains the timer, ensure initial render is consistent
  if (getTimerEl()) renderTime();
})();