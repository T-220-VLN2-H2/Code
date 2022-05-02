const notes = new Map();
const tunes = new Map();
const recording = new Map()
const recording_arr = new Array()
notes.set("a", "c4");
notes.set("w", "c#4");
notes.set("s", "d4")
notes.set("e", "d#4");
notes.set("d", "e4");
notes.set("f", "f4");
notes.set("t", "f#4");
notes.set("g", "g4");
notes.set("y", "g#4");
notes.set("h", "a4");
notes.set("u", "bb4");
notes.set("j", "b4");
notes.set("k", "c5");
notes.set("o", "c#5");
notes.set("l", "d5");
notes.set("p", "d#5");
notes.set(";", "E5");
notes.set("æ", "e5");
var record = false;
var synth = new Tone.Synth().toDestination();
var url = 'https://veff2022-h1.herokuapp.com/api/v1/tunes';
var timing = 0;
var difference = 0;
var down = false;
var playing = false;
document.addEventListener("keydown", PlayNotePress);
document.addEventListener("keydown", press_button);
document.addEventListener("keyup", stop_pressing_button);

function press_button(e) {
    down = true;
    const activeTextarea = document.activeElement;
    if (getNote(e.key) !== undefined){
        if (activeTextarea.id != "recordName"){
        var element = document.getElementById(getNote(e.key));
        element.classList.add("press-button");}
    }
}

function stop_pressing_button(e) {
    down = false;
    if (getNote(e.key) !== undefined){
        var element = document.getElementById(getNote(e.key));
        element.classList.remove("press-button");
    }
}

function PlayNoteClick (n) {
    // n is id of the tune to be played
    var now = Tone.now();
    synth.triggerAttackRelease(n,"8n",now);
    if (record){
        var timing = Tone.now()
        var bit = Object()
        bit.note = n
        bit.duration = '8n'
        bit.timing = timing
        now = Tone.now()
        recording_arr.push(bit) 
    }
};

function PlayNotePress (e) {
    console.log(playing)
    if (playing === true) {
        return undefined;
    } 
    const activeTextarea = document.activeElement;
    if (activeTextarea.id != "recordName"){
            if (getNote(e.key) !== undefined && down === false) {
                var play_now = Tone.now()
                synth.triggerAttackRelease(getNote(e.key), "8n", play_now);
            if (record){
                if (recording_arr.length === 0) {
                    difference = play_now
                }
                var bit = Object()
                bit.note = getNote(e.key)
                bit.duration = '8n'
                bit.timing = play_now - difference
                now = Tone.now()
                recording_arr.push(bit)
            }
        }
    }
};


function getNote(key) {
    return notes.get(key);
};

function getAllTunes() {
    //Perform a GET request to the url
    axios.get(url)
        .then(function (response) {
            for (var i=0; i<response.data.length; i++) {
                var tunesDrop = document.getElementById("tunesDrop");
                var title = document.createElement('option');
                title.text = response.data[i].name;
                tunesDrop.add(title);
                tunes.set(response.data[i].name, response.data[i].tune)
            
            }
        })
}

function getTune(key) {
    return tunes.get(key)
}

function playTune() {
    playing = true;
    selected = document.getElementById("tunesDrop")
    selected_tune = getTune(selected.value)
    for (var i=0; i<selected_tune.length; i++) {
        var now = Tone.now();
        synth.triggerAttackRelease(selected_tune[i].note,selected_tune[i].duration,now + selected_tune[i].timing), selected_tune[i].timing;
        console.log(playing)
    }
}

function start_record() {
    stopbtn = document.getElementById("stopbtn");
    stopbtn.disabled = false
    record = true;
    recording_arr.length = 0;
    }  


function stop_record() {
    stopbtn = document.getElementById("stopbtn");
    stopbtn.disabled = true;
    record = false;
    if (recording_arr.length !== 0){
        var recordName = document.getElementById("recordName").value;
        var title = document.createElement('option');
        if (recordName === '') {
            recordName = 'Unnamed Tune'
        }
        title.text = recordName;
        tunesDrop.add(title);
        tunes.set(recordName, recording_arr)
        post_map = new Map()
        post_map.set(recordName, recording_arr)
        uploadTune(post_map)
    }
}

function uploadTune(tune_map) {
    for (const name of tune_map.keys()) {
        var title = name
    }
    var arr = tune_map.get(title)
    axios.post('https://veff2022-h3.herokuapp.com/api/v1/tunes', {
        name: title,
        tune: arr
      })
}

function getByValue(map, searchValue) {
    for (let [key, value] of map.entries()) {
      if (value === searchValue)
        return key;
    }
  }


function press_button_for_playback(note) {
        key = getByValue(notes, note)
        var element = document.getElementById(getNote(key));
        element.classList.add("press-button");
    }

function release_button_for_playback(note) {
        key = getByValue(notes, note)
        var element = document.getElementById(getNote(key));
        element.classList.remove("press-button");
    }


function add_recording(recording) {
    tunesDrop.add(title);
    tunes.set(response.data[i].name, response.data[i].tune)
    tunes.set(recording.key, recording.ar)
}