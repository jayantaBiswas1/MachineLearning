function draw(slope, intercept) {
  var points = [];
  const canvas = document.querySelector('#canvas');

  if (!canvas.getContext) {
      return;
  }
  const ctx = canvas.getContext('2d');

  // set line stroke and line width
  ctx.strokeStyle = 'red';
  ctx.lineWidth = 5;

  // draw a red line
  ctx.beginPath();
  var x = 100;
  var y = intercept;
  //alert(intercept);
  //alert(x);
  //alert(slope);
  ctx.moveTo(x, intercept);
  var x2 = 300;
  //console.log(slope * x2 + intercept);
  //console.log(parseInt(intercept));

  var y2 = slope * x2 + parseInt(intercept);
  y2 = y2* -1;
  
  //alert(x2);
  //alert(y2);
  ctx.lineTo(x2, y2);
  ctx.stroke();  
  //points[0] = x;
  //points[1] = y;
  //points[2] = x2;
  //points[3] = y2;
  return points;
}
//draw();