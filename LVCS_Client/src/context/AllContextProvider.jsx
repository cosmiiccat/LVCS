import React from "react";
import { useState } from "react";
import AllContext from "./AllContext";

function AllContextProvider({ children }) {
    const data = {
        public: {
          "index.html": "",
          "favicon.ico": "",
        },
        src: {
          components: {
            Header: {
              "HeaderComponent.js": "",
              "HeaderComponent.css": "",
            },
            Footer: {
              "FooterComponent.js": "",
              "FooterComponent.css": "",
            },
            Navigation: {
              "NavComponent.js": "",
              "NavComponent.css": "",
            },
            "...": {},
          },
          pages: {
            Home: {
              "HomePage.js": "",
              "HomePage.css": "",
            },
            About: {
              "AboutPage.js": "",
              "AboutPage.css": "",
            },
            Contact: {
              "ContactPage.js": "",
              "ContactPage.css": "",
            },
            "...": {},
          },
          "App.js": "",
          "index.js": "",
          "index.css": "",
        },
        "package.json": "",
        "README.md": "",
        "CommitMessage": "Initial Commit",
        "CommitDate": "2021-08-01",
      };
      
    const [currentDirectory, setCurrentDirectory] = useState("");
    const [currentData, setCurrentData] = useState(data);
    const [INITpath, setINITpath] = useState("");


    return (
        <AllContext.Provider value={{
            currentDirectory,
            setCurrentDirectory,
            currentData,
            setCurrentData,
            data,
            INITpath,
            setINITpath,
            
        }}>
        {children}
        </AllContext.Provider>
    ); 
}

export default AllContextProvider;