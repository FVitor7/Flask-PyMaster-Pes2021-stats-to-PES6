//// new code 

function imgError(image) {
  image.onerror = "";
  image.src = "https://pesmaster.fra1.cdn.digitaloceanspaces.com/players/pes-2021/player_0.png";
  return true;
}


function getBaseUrl() {
  // Nome do host
  var hostName = location.hostname;

  if (hostName === "localhost") {
    // Endereço após o domínio do site
    pathname = window.location.pathname;
    // Separa o pathname com uma barra transformando o resultado em um array
    splitPath = pathname.split('/');

    // Obtém o segundo valor do array, que é o nome da pasta do servidor local
    path = splitPath[1];

    baseUrl = "http://" + hostName + ":5000"
    //+ path;
  } else {
    baseUrl = "https://" + hostName;
  }

  return baseUrl;
}

baseUrl = getBaseUrl();
console.log(baseUrl)

document.getElementById('copy_button').style.display = 'none';


function printHexagon(attack, technique, stamina, defence, balance, acceleration) {
  var ctx = document.getElementById("myChart")

  var data = {
    labels: ["ATQ", "TEC", "RES", "DEF", "FOR", "VCD"],
    datasets: [{
      data: [attack, technique, stamina, defence, balance, acceleration].map(function (stat) {
        return calculateStatForHexagon(stat)
      }),
      borderColor: [
        'rgb(253,182,180)'
      ],
      borderWidth: 3,
      pointRadius: 0,
    },
    {
      data: [20, 20, 20, 20, 20, 20],
      backgroundColor: '#424242',
      pointRadius: 0
    },
    {
      data: [40, 40, 40, 40, 40, 40],
      backgroundColor: '#5e5e5e',
      pointRadius: 0
    },
    {
      data: [60, 60, 60, 60, 60, 60],
      backgroundColor: '#424242',
      pointRadius: 0
    },
    {
      data: [80, 80, 80, 80, 80, 80],
      backgroundColor: '#5e5e5e',
      pointRadius: 0
    },
    {
      data: [100, 100, 100, 100, 100, 100],
      backgroundColor: '#424242',
      pointRadius: 0
    }]
  }

  var options = {
    scale: {
      ticks: {
        display: false,
        beginAtZero: true,
        min: 0,
        max: 100,
        stepSize: 20
      },
      pointLabels: {
        fontSize: 12
      }
    },
    legend: {
      display: false,
      responsive: true,
      maintainAspectRatio: false
    }
  }

  var radarChart = new Chart(ctx, {
    type: 'radar',
    data: data,
    options: options
  })
}

function calculateStatForHexagon(stat) {
  if (stat <= 39) {
    convertedStat = stat * 0.5
  } else if (stat >= 40 && stat <= 64) {
    convertedStat = ((stat - 39) * 0.8) + 20
  } else if (stat >= 65 && stat <= 68) {
    convertedStat = ((stat - 65) * 2) + 42
  } else if (stat >= 69 && stat <= 79) {
    convertedStat = stat - 19
  } else if (stat >= 80 && stat <= 89) {
    convertedStat = ((stat - 80) * 2) + 62
  } else if (stat >= 90 && stat <= 99) {
    convertedStat = ((stat - 90) * 2) + 82
  }
  return convertedStat
}


function formatStatsToCopy(stats) {
  let formatStats = `<img src="${stats['img_player']}" onerror="imgError(this);">`
  formatStats += "<canvas id='myChart' style='height:400px; width:400px'></canvas>" + "<br>"
  formatStats += "Name: " + stats["name"] +
  "<br>"
  formatStats += "Nationality: " + stats["nation"] + "<br>"

  formatStats += "Positions: " + stats["positions"] + "<br>"
  formatStats += "Registred Positions: <b><font color ='FFFB44'>★</font></b>" + stats["Position"] + "<br><br>"
  formatStats += "Age: " + stats["Age"] + "<br>"

  formatStats += "Height: " + stats["Height"] + "<br>"
  formatStats += "Weight: " + stats["Weight"] + "<br>" + "<br>"

  formatStats += "Injury Tolerance: " + stats["injury"] + "<br>"

  formatStats += "Foot: " + stats["Stronger_Foot"] + "<br>"

  if (stats["Stronger_Foot"] == "L") {
    formatStats += "Side: R" + "<br>" + "<br>"
  } else {
    formatStats += "Side: L" + "<br>" + "<br>"
  }


  formatStats += "Attack: " + putColor(stats["attack"]) + "<br>"

  formatStats += "Defence: " + putColor(stats["defence"]) + "<br>"
  formatStats += "Balance: " + putColor(stats["balance"]) + "<br>"
  formatStats += "Stamina: " + putColor(stats["stamina"]) + "<br>"
  formatStats += "Speed: " + putColor(stats["speed"]) + "<br>"
  formatStats += "Acceleration: " + putColor(stats["acceleration"]) + "<br>"
  formatStats += "Response: " + putColor(stats["response"]) + "<br>"
  formatStats += "Agility: " + putColor(stats["agility"]) + "<br>"
  formatStats += "Dribble Accuracy: " + putColor(stats["dribble_accuracy"]) + "<br>"
  formatStats += "Dribble Speed: " + putColor(stats["dribble_speed"]) + "<br>"
  formatStats += "Short Pass Accuracy: " + putColor(stats["short_pass_accuracy"]) + "<br>"
  formatStats += "Short Pass Speed: " + putColor(stats["short_pass_speed"]) + "<br>"
  formatStats += "Long Pass Accuracy: " + putColor(stats["long_pass_accuracy"]) + "<br>"
  formatStats += "Long Pass Speed: " + putColor(stats["long_pass_speed"]) + "<br>"
  formatStats += "Shot Accuracy: " + putColor(stats["shot_accuracy"]) + "<br>"
  formatStats += "Shot Power: " + putColor(stats["shot_power"]) + "<br>"
  formatStats += "Shot Technique: " + putColor(stats["shot_technique"]) + "<br>"
  formatStats += "Free Kick Accuracy: " + putColor(stats["free_kick_accuracy"]) + "<br>"
  formatStats += "Swerve: " + putColor(stats["swerve"]) + "<br>"
  formatStats += "Heading: " + putColor(stats["heading"]) + "<br>"
  formatStats += "Jump: " + putColor(stats["jump"]) + "<br>"
  formatStats += "Technique: " + putColor(stats["technique"]) + "<br>"
  formatStats += "Aggression: " + putColor(stats["aggression"]) + "<br>"
  formatStats += "Mentality: " + putColor(stats["mentality"]) + "<br>"
  formatStats += "GK Skills: " + putColor(stats["gk_skills"]) + "<br>"
  formatStats += "Team work: " + putColor(stats["team_work"]) + "<br>" + "<br>"
  formatStats += "Consistency: " + stats["consistency"] + "<br>"
  formatStats += "Condition/Fitness: " + stats["condition"] + "<br>"
  formatStats += "Weak Foot Accuracy: " + stats["weak_foot_accuracy"] + "<br>"
  formatStats += "Weak Foot Frequency: " + stats["weak_foot_frequency"] + "<br>" + "<br>"
  formatStats += "Free kick style: " + stats["free_kick_style"] + "<br>"
  formatStats += "Drop kick style: " + stats["drop_kick_style"] + "<br>"
  formatStats += "Dribbling style: " + stats["dribbling_style"] + "<br>"
  formatStats += "Penalty style: " + stats["penalty_style"] + "<br>" + "<br>"


  formatStats += "SPECIAL ABILITIES: <br>"
  var special_abilities = stats["special_abilities"];
  var special_abilities = special_abilities.split(',');
  formatStats += formatSpecialAbilities(special_abilities)

  console.log(formatStats)

  return formatStats
}

function putColor(stat) {
  let color = "000000"
  if (stat >= 75 && stat <= 79) {
    color = "00821D"
  } else if (stat >= 80 && stat <= 89) {
    color = "FFFB44"
  } else if (stat >= 90 && stat <= 94) {
    color = "FF841E"
  } else if (stat >= 95 && stat <= 99) {
    color = "FF1301"
  }
  return '<b><font color=' + color + '>' + stat + '</font></b>'
}

function formatSpecialAbilities(specialAbilities) {

  let formatSpecialAbilities = ""
  console.log(specialAbilities)
  specialAbilities.forEach(function (specialAbility) {
    formatSpecialAbilities += "<b><font color ='FFFB44'>★</font>" + specialAbility + "</b><br>"
  })
  return formatSpecialAbilities
}

function get_json(data) {


  var xhr = new XMLHttpRequest();
  var url = baseUrl + "/api/v1/players/pes6/";
  xhr.open("POST", url, true);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var stats = JSON.parse(xhr.responseText);
      console.log(stats);
      var div_stats = document.getElementById("statsToCopy");


      div_stats.innerHTML = "";

      div_stats.innerHTML = formatStatsToCopy(stats);

      thirdStats = formatStatsToCopy(stats)
      let statsToCopy = '#statsToCopy'
      $(statsToCopy).html(thirdStats)
      $(statsToCopy).addClass("text")

      document.getElementById('copy_button').style.display = 'inline';


      var atk = stats["attack"]

      var tec = stats["technique"]

      var sta = stats["stamina"]

      var def = stats["defence"]

      var bal = stats["balance"]

      var acc = stats["acceleration"]
      printHexagon(atk, tec, sta, def, bal, acc)

      $(document).ready(function () {
        window.location.href = '#foo';
      });
    }

  };
  xhr.send(data);
}




function get_stats_table(pl_link) {
  $('html,body').scrollTop(0);
  //console.log(pl_link)
  document.getElementById('copy_button').style.display = 'none';
  var div_stats = document.getElementById("statsToCopy");

  div_stats.innerHTML = "";

  document.getElementById('copy_button').style.display = 'none';



  var player_name = pl_link
  console.log(player_name);

  var version_player = 'pes6'


  var data = JSON.stringify({ "player_id": player_name });

  get_json(data)

};


function getGraphsToShow(stats) {
  let formatStats = getImgTag(stats["soFifaId"], false) + "<br><br>"
  formatStats += "<canvas id='myChart' style='height:400px; width:400px'></canvas>" + "<br>"
  return formatStats
}


function copyToClipboard() {
  let text = $(statsToCopy).clone().find('br').prepend('\r\n').end().text()
  element = $('<textarea>').appendTo('body').val(text).select()
  document.execCommand('copy')
  element.remove()
}


/// old code

function load_json(pl_name, tm_name, nat_name) {
  url = baseUrl + '/api/v1/?name=' + pl_name + '&team=' + tm_name + '&nation=' + nat_name;
  $.getJSON(url, function (result) {
    // result é o json obtido
    $(document).ready(function () {
      for (i = 0; i < result.length; i++) {
        line = createLine(result[i]);
        $('#customers tbody').append(line);
      }
    });
  });
}

var timer = null;
$('#text_player_name').keyup(function () {
  clearTimeout(timer);
  timer = setTimeout(search_pl, 1000)
});

$('#text_team_name').keyup(function () {
  clearTimeout(timer);
  timer = setTimeout(search_pl, 1000)
});

$('#text_nation_name').keyup(function () {
  clearTimeout(timer);
  timer = setTimeout(search_pl, 1000)
});


function search_pl() {

  pl_name = document.getElementById('text_player_name').value
  tm_name = document.getElementById('text_team_name').value
  nat_name = document.getElementById('text_nation_name').value

  $("#statsToCopy").empty()
  $("#tbodyid").empty()
  
  load_json(pl_name, tm_name, nat_name)



};

function createLine(obj) {
  var position = '';
  if (obj.pos == 0) {
    position = 'GK'
  } else if (obj.pos == 1) {
    position = 'CB'
  } else if (obj.pos == 2) {
    position = 'LB'
  } else if (obj.pos == 3) {
    position = 'RB'
  } else if (obj.pos == 4) {
    position = 'DMF'
  } else if (obj.pos == 5) {
    position = 'CMF'
  } else if (obj.pos == 6) {
    position = 'LMF'
  } else if (obj.pos == 7) {
    position = 'RMF'
  } else if (obj.pos == 8) {
    position = 'AMF'
  } else if (obj.pos == 9) {
    position = 'LWF'
  } else if (obj.pos == 10) {
    position = 'RWF'
  } else if (obj.pos == 11) {
    position = 'SS'
  } else if (obj.pos == 12) {
    position = 'CF'
  }


  var url_base = 'https://www.pesmaster.com';

  var line = `'<tr <a target="_blank" class="namelink" onclick="get_stats_table('${obj.id}')"></a>>'
    '<th scope="row"><img src="${url_base}${obj.image}" onerror="imgError(this);" style="width: auto; height: auto;max-width: 70px;max-height: 70px"></th>'
    '<td>${obj.name}</td>'
    '<td>${obj.age}</td>'
    '<td>${obj.over}</td>'
    '<td>${obj.pos}</td>'
    '</tr>'`;
  return line;
}

load_json('', '', '')
