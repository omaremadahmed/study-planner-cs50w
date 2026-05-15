(() => {
  const rootEl = document.getElementById("react-root");
  if (!rootEl) return;
  if (!window.React || !window.ReactDOM) return;

  const { createElement: h, useEffect, useMemo, useState } = window.React;

  function StudyWidget() {
    const tips = useMemo(
      () => [
        "Use 25 minutes focus + 5 minutes break.",
        "Write the smallest next step before you start.",
        "Group similar tasks to reduce context switching.",
        "Review your subjects list and pick the top 1 priority.",
      ],
      [],
    );

    const [now, setNow] = useState(() => new Date());
    const [dismissed, setDismissed] = useState(() => {
      try {
        return localStorage.getItem("sp_widget_dismissed") === "1";
      } catch {
        return false;
      }
    });

    useEffect(() => {
      const t = setInterval(() => setNow(new Date()), 1000 * 30);
      return () => clearInterval(t);
    }, []);

    const tip = tips[now.getDate() % tips.length];

    if (dismissed) return null;

    return h(
      "div",
      { className: "react-card d-flex align-items-center justify-content-between gap-3 flex-wrap" },
      h("div", null,
        h("div", { className: "fw-bold" }, "Study Planner"),
        h("div", { className: "meta" }, `${now.toLocaleDateString()} • ${tip}`),
      ),
      h(
        "div",
        { className: "d-flex gap-2" },
        h(
          "button",
          {
            className: "btn btn-sm btn-outline-light",
            onClick: () => setNow(new Date()),
            type: "button",
          },
          "Refresh",
        ),
        h(
          "button",
          {
            className: "btn btn-sm btn-outline-light",
            onClick: () => {
              try {
                localStorage.setItem("sp_widget_dismissed", "1");
              } catch {}
              setDismissed(true);
            },
            type: "button",
          },
          "Dismiss",
        ),
      ),
    );
  }

  try {
    const root = window.ReactDOM.createRoot(rootEl);
    root.render(h(StudyWidget));
  } catch {
    // If React fails for any reason, don't break the page.
  }
})();

