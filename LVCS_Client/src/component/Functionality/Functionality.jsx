import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useRef, useState } from "react";
import { useContext } from "react";
import axios from "axios";

import AllContext from "../../context/AllContext";

import logo from "../../assets/github-mark.svg";

import "./Functionality.css";
import ContentPage from "../ContentPage/ContentPage";
import RepositoryPage from "../RepositoryPage/RepositoryPage";
function Functionality() {
  const { INITpath, setINITpath } = useContext(AllContext);
  const navigate = useNavigate();
  const [additionalComponent, setAdditionalComponent] = useState(false);
  const [additionalComponentforInit, setAdditionalComponentforInit] =
    useState(false);
  const [additionalComponentforCommit, setAdditionalComponentforCommit] =
    useState(false);
  const [additionalComponentforConfig, setAdditionalComponentforConfig] = useState(false);
  const [additionalComponentforPush, setAdditionalComponentforPush] = useState(false);

  const [pathUrl, setPathUrl] = useState("");
  const [pathUrlforInit, setPathUrlforInit] = useState("");
  const [pathExist, setPathExist] = useState(false);
  const [payload, setPayload] = useState({});
  const [payloadforPULL, setPayloadforPULL] = useState({});
  const [commitPayload, setCommitPayload] = useState({});
  const [commitMessage, setCommitMessage] = useState("");
  const [commitStatus, setCommitStatus] = useState(false);
  const [pushStatus, setPushStatus] = useState(false);
  const [currentStatus, setCurrentStatus] = useState("local");

  const [configStatus, setConfigStatus] = useState(false);
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");

  const [repo_name, setRepoName] = useState("");
  const [password, setPassword] = useState("");


  const pathRef = useRef(null);
  const parthRefforInit = useRef(null);
  const commitRef = useRef(null);

  const handleINITbutton = () => {
    setAdditionalComponentforInit(true);
  };

  const handlePUSH = () => {
    setAdditionalComponentforPush(!additionalComponentforPush);
  };

  useEffect(() => {
    const localButton = document.querySelector(".local-button");
    const remoteButton = document.querySelector(".remote-button");

    if(currentStatus === "local"){
      localButton.classList.add("active");
      remoteButton.classList.remove("active");
    }
    if(currentStatus === "remote"){
      remoteButton.classList.add("active");
      localButton.classList.remove("active");
    }
  }, [currentStatus]);

  const handleLocal = () => {
    setCurrentStatus("local");
  };

  const handleRemote = () => {
    setCurrentStatus("remote");
  };


  const handleADDbutton = () => {
    axios
      .post("http://127.0.0.1:8000/lvcs/add", payload)
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handleCOMMITbutton = () => {
    setAdditionalComponentforCommit(!additionalComponentforCommit);
  };

  const handleCommitMessage = () => {
    if (!commitMessage) return;
    setCommitStatus(true);
    console.log("This is the commit message: ", commitMessage);
    const COMMITpayload = {
      path: pathUrl,
      commit: true,
      commit_message: commitMessage,
    };
    setCommitPayload(COMMITpayload);
    axios
      .post("http://127.0.0.1:8000/lvcs/commit", COMMITpayload)
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    setAdditionalComponentforCommit(!additionalComponentforCommit);
  };

  const handlePULLbutton = () => {
    console.log("This is the payload: ", payloadforPULL);
    axios
    .post("http://127.0.0.1:8000/lvcs/pull", payloadforPULL,{headers: {}})
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handlePUSHbutton = () => {
    const pushPayload = {
      path: pathUrl,
      repo_name: repo_name,
      password: password
    };  



    console.log("This is the payload: ", payload);
    axios
    .post("http://127.0.0.1:8000/lvcs/push", pushPayload ,{headers: {}})
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handleCLONEbutton = () => {
    console.log("This is the payload: ", payload);
    axios
    .post("http://127.0.0.1:8000/lvcs/clone", payload)
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const handleCONFIGbutton = () => {
    setAdditionalComponentforConfig(!additionalComponentforConfig);
  }

  const handleConfig = () => {
    if (!username || !email) return;
    setConfigStatus(true);
    console.log("This is the username: ", username);
    console.log("This is the email: ", email);
    const CONFIGpayload = {
      path: pathUrl,
      username: username,
      email: email,
    };
    axios
      .post("http://127.0.0.1:8000/lvcs/config",CONFIGpayload)
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
    setAdditionalComponentforConfig(!additionalComponentforConfig);
  };




  const consoleLog = (data) => {
    const ul = document.querySelector(".lines");
    const div = document.createElement("div");
    const span = document.createElement("span");
    const p = document.createElement("p");

    if(data.success === "false"){
      p.className = "error";
      p.textContent = data.error;
    }else{
      p.className = "success";
      let dataString = JSON.stringify(data.data);

// Set the text content of the HTML element
p.textContent = dataString;
    }

    div.className = "console-log-message";
    span.className = "console-log";
    span.textContent = pathUrl;
    // p.textContent = data.message;
    div.append(span, p);
    ul.appendChild(div);
  };


  const handlePath = () => {
    if(pathUrl.length === 0) return;
    const payload = {
      path: pathUrl,
      repo_name: "testing3",
      password: "password",
    };
    const payloadforPath = {
      path: pathUrl,
    };
    setPayload(payload);
    setPayloadforPULL(payload);
    setPathExist(true);
  }

  useEffect(() => {
    console.log("This is the paylaod for pull: ", payloadforPULL);
  }, [payloadforPULL]);

  const handlePathExist = () => {
    if (!pathExist) setPathUrl(pathUrl);
    if (!pathUrl) return;
    setPathExist(true);
    setINITpath(pathUrl);
    const payload = {
      path: pathUrl,
    };
    setPayload(payload);
    console.log("This is path", pathUrl);
    console.log(payload);

    axios
      .post("http://127.0.0.1:8000/lvcs/init", payload)
      .then((res) => {
        console.log(res);
        consoleLog(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  useEffect(() => {
    console.log("This is the path: ", pathUrl);
  }, [pathUrl]);

  return (
    <div className="Parent">

      <div className="nav-bar">
        <button className="local-button" onClick={handleLocal}>local</button>
        <button className="remote-button" onClick={handleRemote}>remote</button>
      </div>

    {currentStatus === "local" ? (
    <div className="FunctionalityParentContainer">
      <div className="MainPageMainContainer">
        <div className="LVCS-Logo">
          <img src={logo} alt="LVCS Logo" />
        </div>

        {/* {additionalComponentforInit && ( */}
        {/* {pathExist === true ? ( */}
        <div className="PathContainer">
          <input
            type="text"
            className="Path"
            placeholder="Enter the path"
            value={pathUrl}
            onChange={(e) => setPathUrl(e.target.value)}
          />
          <div className="set-reset-buttons">
            <button
              className="Submit-Button Set-Button"
              onClick={handlePath}
            >
              Set
            </button>
          </div>
        </div>
        {/* ) : ( <div className="pathexist"><p>path is already set!!</p></div> */}
        {/* )} */}
        

        {/* )} */}

        {additionalComponentforCommit &&
          (commitStatus ? (
            <div className="CommitContainer PathContainer"> Last Commit: <span className="Last-Commit">{commitMessage}</span> </div>
          ) : (
            <div className="CommitContainer PathContainer">
              <input
                type="text"
                className="commit-message Path"
                placeholder="Enter commit message"
                value={commitMessage}
                onChange={(e) => setCommitMessage(e.target.value)}
              />
              <div className="set-commit-message-button">
                <button
                  className="Submit-Button Set-Button commit-button"
                  onClick={handleCommitMessage}
                >
                  Commit Changes
                </button>
              </div>
            </div>
          ))}

{additionalComponentforConfig &&
          (configStatus ? (
            <div className="ConfigContainer PathContainer"> Config Success </div>
          ) : (
            <div className="ConfigContainer PathContainer">
              
              <input
                type="text"
                className="commit-message Path"
                placeholder="Enter your username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />

<input
                type="text"
                className="commit-message Path "
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
              <div className="set-commit-message-button">
                <button
                  className="Submit-Button Set-Button commit-button"
                  onClick={handleConfig}
                >
                  Config
                </button>
              </div>
            </div>
          ))}

{additionalComponentforPush &&
          (pushStatus ? (
            <div className="PushContainer PathContainer"> Successfully pushed </div>
          ) : (
            <div className="PushContainer PathContainer">
              <input
                type="text"
                className="push-input commit-message Path"
                placeholder="Enter repository name"
                value={repo_name}
                onChange={(e) => setRepoName(e.target.value)}
              />

              <input
                type="text"
                className="password-input commit-message Path"
                placeholder="Enter password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              <div className="set-commit-message-button">
                <button
                  className="Submit-Button Set-Button commit-button"
                  onClick={handlePUSHbutton}
                >
                  Push Changes
                </button>
              </div>
            </div>
          ))}

        

        <div className="ButtonAndInput">
          <div className="ButtonContainer">
            <div className="row">
              <button className="function-button" onClick={handleCONFIGbutton}>
                config
              </button>
              <button className="function-button" onClick={handlePathExist}>
                init
              </button>
              <button className="function-button" onClick={handleADDbutton}>
                add
              </button>
              <button className="function-button" onClick={handleCOMMITbutton}>
                commit
              </button>
            </div>
            <div className="row">
              <button className="function-button" onClick={handlePULLbutton}>
                pull
              </button>
              <button className="function-button" onClick={handlePUSH}>
                push
              </button>
              <button className="function-button" onClick={handleCLONEbutton}>
                clone
              </button>
            </div>
          </div>

          {additionalComponent && (
            <div className="Take-Input" ref={pathRef}>
              <input
                type="text"
                className="Path"
                placeholder="Enter the path"
                value={pathUrl}
                onChange={(e) => setPathUrl(e.target.value)}
              />
              <button className="Submit-Button">Submit</button>
            </div>
          )}
        </div>
      </div>
      <div className="ExtraThing console">
        <div className="console-heading">
          <h1>Console</h1>
        </div>
        <ul className="lines"></ul>
      </div>
    </div>
    ) :(
      <div className="RepositoryPage-Component">
        <RepositoryPage/>
      </div>
    )}
    </div>
  );
}

export default Functionality;
