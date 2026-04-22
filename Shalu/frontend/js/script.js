
let recorder;
let audioChunks=[];

const record=document.getElementById("record");
const stop=document.getElementById("stop");
const result=document.getElementById("result");
const status=document.getElementById("status");

record.onclick = async () => {

const stream = await navigator.mediaDevices.getUserMedia({audio:true});

recorder = new MediaRecorder(stream);

recorder.start();

status.innerText="Recording...";

audioChunks=[];

recorder.ondataavailable = e=>{

audioChunks.push(e.data);

};

};

stop.onclick = ()=>{

recorder.stop();

status.innerText="Processing...";

recorder.onstop = async ()=>{

const blob = new Blob(audioChunks,{type:"audio/wav"});

const formData = new FormData();

formData.append("file",blob,"voice.wav");

const response = await fetch("http://127.0.0.1:5000/predict",{
method:"POST",
body:formData
});

const data = await response.json();

result.innerText="Detected Emotion: "+data.emotion;

status.innerText="Done";

};

};
