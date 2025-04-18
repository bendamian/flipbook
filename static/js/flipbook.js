$(window).on("load", function () {
  // Initialize the flipbook
  $("#flipbook").turn({
    width: 1200,
    height: 800,
    autoCenter: true,
    display: "double",
    acceleration: true,
    gradients: true
  });

  // Zoom slider logic
  $("#zoomRange").on("input", function () {
    const scale = $(this).val() / 100;
    $("#flipbook").css({
      transform: `scale(${scale})`,
      transformOrigin: "top center"
    });
  });
});
