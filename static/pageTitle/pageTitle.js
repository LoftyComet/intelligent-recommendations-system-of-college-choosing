// 全局变量
var pageTitle;
var mouseIsMoved;
var titleSize=42;

var backgroundColor='#9ed0c9';
var frontColor_moved='#ebfffd';
var frontColor_not_moved='#cae5e2';
var maxStep=60;//[0,10] [move,not move]
var cntStep=maxStep;
var frontColor=frontColor_not_moved;

let followMouseFactor=0.99;

let w;//=max(720,width);
let h;//=height;
let scaleFactor;//=Math.sqrt(w/1920);

var cones=[];
var bigRects=[];
var rects=[];
var tris=[];
var ws=[];

//-----------------------------
function setup() 
{
	createCanvas(windowWidth, windowHeight);
	setShapeSize();
//   let myCanvas =createCanvas(400, 400);
//  myCanvas.parent('pageTitle');


	cones.push([1/7,0,77.5*1.3,27.5*1.3,PI/3],[-0.45,-0.4,77.5*1.2,27.5*1.2,-PI/4]);
	bigRects.push([-0.3,-1/4,150,-PI/4],[0.22,0.55,120,-PI/3]);
	rects.push([-0.176,-0.24,60,PI*0.4],[0.5,0.3,50,PI*1.4]);
	tris.push([0.316,0,155,155,PI],[-0.416,0.4,155,155,PI*0.8]);
	ws.push([-0.15,0.2,40,-PI/6],[0.4,-0.38,30,PI/6]);

	let fr=window.parent.document.getElementById("pageTitle");
	let name0=fr.name;
	pageTitle="";
	for(c in name0)
	{
		pageTitle+=name0[c];
		if(c!=name0.length-1)
		pageTitle+="   ";
	}
}

function draw() 
{
	background(backgroundColor);

	for( cone of cones)
	{
		let x=cone[0]*w+width/2;
		let y=cone[1]*h+height/2;
		x=mouseX+(x-mouseX)*followMouseFactor;
		y=mouseY+(y-mouseY)*followMouseFactor;

		draw_cone(x,y,cone[2]*scaleFactor,cone[3]*scaleFactor,cone[4]);
	}

	for(bigRect of bigRects)
	{
		let x=bigRect[0]*w+width/2;
		let y=bigRect[1]*h+height/2;
		x=mouseX+(x-mouseX)*followMouseFactor;
		y=mouseY+(y-mouseY)*followMouseFactor;
		// window.alert(x,y);
		draw_bigRect(x,y,bigRect[2]*scaleFactor,bigRect[3]);
	}

	for(myrect of rects)
	{
		let x=myrect[0]*w+width/2;
		let y=myrect[1]*h+height/2;
		x=mouseX+(x-mouseX)*followMouseFactor;
		y=mouseY+(y-mouseY)*followMouseFactor;
		draw_rect(x,y,myrect[2],myrect[3]);
	}

	for(tri of tris)
	{
		let x=tri[0]*w+width/2;
		let y=tri[1]*h+height/2;
		x=mouseX+(x-mouseX)*followMouseFactor;
		y=mouseY+(y-mouseY)*followMouseFactor;
		draw_tri(x,y,tri[2]*scaleFactor,tri[3]*scaleFactor,tri[4]);
	}

	for(ww of ws)
	{
		let x=ww[0]*w+width/2;
		let y=ww[1]*h+height/2;
		x=mouseX+(x-mouseX)*followMouseFactor;
		y=mouseY+(y-mouseY)*followMouseFactor;
		draw_w(x,y,ww[2]*scaleFactor,ww[3]);
	}

	let textW=textWidth(pageTitle);
	noStroke();
	fill(118, 168, 161,128);
	rectMode(CENTER);
	rect(width/2,height/2,textW*1.2,titleSize*1.5,20);
	
	textSize(titleSize);
	textAlign(CENTER, CENTER);
	fill(14, 54, 85);
	text(pageTitle, width/2, height/2);

	mouseIsMoved=false;
	if(cntStep<maxStep) cntStep++;
	frontColor=lerpCo(frontColor_moved,frontColor_not_moved,cntStep/maxStep);
}

function windowResized() 
{
	resizeCanvas(windowWidth, windowHeight);
	setShapeSize();
}

function setShapeSize()
{
	w=max(720,width);
	h=height;
	scaleFactor=Math.sqrt(w/1920);
}

function mouseMoved() 
{
	mouseIsMoved=true;
	frontColor=frontColor_moved;
	cntStep=0;
	return false;
}
//------------------------
function lerpCo(from,to,a)
{
	let r1=red(from),r2=red(to);
	let r=r1+(r2-r1)*cntStep/maxStep;
	let g1=green(from),g2=green(to);
	let g=g1+(g2-g1)*cntStep/maxStep;
	let b1=green(from),b2=green(to);
	let b=b1+(b2-b1)*cntStep/maxStep;
	return color(r,g,b);
}

function draw_cone(x,y,a2,b2,r)
{
	let h=a2;
	push();
	translate(x,y);
	rotate(r);
	stroke(frontColor);
	strokeWeight(4);
	fill(backgroundColor);
	triangle(-a2/2,h/2,a2/2,h/2,0,-h/2);
	strokeWeight(5);
	ellipse(0, h/2,a2 ,b2 );
	pop();	
}

function draw_bigRect(x,y,a,r)
{
	push();
	translate(x,y);
	rotate(r);
	stroke(frontColor);
	strokeWeight(4);
	rectMode(CENTER);
	fill(frontColor);
	rect(0,0,a*0.95,a*0.95	);
	stroke(backgroundColor);
	strokeWeight(a*0.6*0.95	/6);
	line(-a/2,-a/2,a/2,a/2);
	let p=6;
	strokeWeight(a*0.3*0.95/p);
	for(var i=1;i<p;i++)
	{
		let w=a/(p-1)*i;
		line(w-a/2,-a/2,-a/2,w-a/2);
		line(-w+a/2,a/2,a/2,-w+a/2);
	}
	pop();	
}

function draw_rect(x,y,a,r)
{
	push();
	translate(x,y);
	rotate(r);
	stroke(frontColor);
	strokeWeight(4);
	rectMode(CENTER);
	noFill();
	rect(-a/4,a/4,a,a);
	rect(a/4,-a/4,a,a);
	pop();	
}

function draw_tri(x,y,d,h,r)
{
	push();
	translate(x,y);
	rotate(r);
	stroke(frontColor);
	strokeWeight(7);
	fill(backgroundColor);
	triangle(-d/2,h/3,d/2,h/3,0,-h*2/3);
	fill(frontColor);
	let k=0.5;
	triangle(-d*k/2,h*k/3,d*k/2,h*k/3,0,-h*k*2/3);
	pop();
}

function draw_w(x,y,a,r)
{
	push();
	translate(x,y);
	rotate(r);
	stroke(frontColor);
	strokeWeight(7);
	// fill(backgroundColor);
	line(0,0,a,a);
	line(0,0,-a,a);
	line(a,a,2*a,0);
	line(-a,a,-2*a,0);
	line(2*a,0,3*a,a);
	line(-2*a,0,-3*a,a);
	pop();
}