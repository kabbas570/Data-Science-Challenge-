//
//  ViewController.swift
//  audioRec
//
//  Created by Asad Khan on 30/06/2021.
//

import UIKit
import AVFoundation
import Accelerate

class ViewController: UIViewController, AVAudioRecorderDelegate, AVAudioPlayerDelegate  {
    
    
    @IBOutlet weak var stopRecordingBtn: UIButton!
    @IBOutlet weak var playBtn: UIButton!
    @IBOutlet weak var buttonLable: UIButton!
    
    var recordingSession: AVAudioSession!
    var audioRecorder: AVAudioRecorder!
    var audioPlayer:AVAudioPlayer!
    var asset :  AVURLAsset!
    
    var trimFileUrl: URL?
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.stopRecordingBtn.isHidden = true
        self.playBtn.isHidden = true
        
        //setup Recorder
        self.setupView()
        
    }
    
    func setupView() {
        recordingSession = AVAudioSession.sharedInstance()
        
        do {
            try recordingSession.setCategory(.playAndRecord, mode: .default)
            try recordingSession.setActive(true)
            recordingSession.requestRecordPermission() { [unowned self] allowed in
                DispatchQueue.main.async {
                    if allowed {
                        self.loadRecordingUI()
                    } else {
                        // failed to record
                    }
                }
            }
        } catch {
            // failed to record
        }
    }
    
    func loadRecordingUI() {
        self.buttonLable.isHidden = false
        self.stopRecordingBtn.isHidden = true
        self.playBtn.isHidden = true
    }
    
    @IBAction func record(_ sender: Any) {
        if audioRecorder == nil {
            startRecording()
        } else {
            finishRecording(success: true)
        }
    }
    
    
    
    func startRecording() {
        let audioFilename = getFileURL()
        self.trimFileUrl = getFileURL()
        let settings = [
            AVFormatIDKey: Int(kAudioFormatMPEG4AAC),
            AVSampleRateKey: 12000,
            AVNumberOfChannelsKey: 1,
            AVEncoderAudioQualityKey: AVAudioQuality.high.rawValue
        ]
        
        do {
            audioRecorder = try AVAudioRecorder(url: audioFilename, settings: settings)
            audioRecorder.delegate = self
            audioRecorder.record()
            
            self.stopRecordingBtn.isHidden = false
        } catch {
            finishRecording(success: false)
        }
    }
    
    func finishRecording(success: Bool) {
        audioRecorder.stop()
        audioRecorder = nil
        
        if success {
            print("Tap to Re-record")
            
        } else {
            
            print("Tap to Record")
            
        }
        
        self.playBtn.isHidden = false
        
    }
    
    @IBAction func stopBtnClicked(_ sender: Any) {
        if audioRecorder == nil {
            startRecording()
        } else {
            finishRecording(success: true)
        }
    }
    
    @IBAction func playBtnClicked(_ sender: Any) {
        if (self.playBtn.titleLabel?.text == "Play"){
            
            self.playBtn.setTitle("Stop", for: .normal)
            preparePlayer()
            audioPlayer.play()
        } else {
            audioPlayer.stop()
            self.playBtn.setTitle("Play", for: .normal)
        }
    }
    
    
    func preparePlayer() {
        var error: NSError?
        do {
            audioPlayer = try AVAudioPlayer(contentsOf: self.trimFileUrl!)
            print(audioPlayer.data)
        } catch let error1 as NSError {
            error = error1
            audioPlayer = nil
        }
        
        if let err = error {
            print("AVAudioPlayer error: \(err.localizedDescription)")
        } else {
            audioPlayer.delegate = self
            
            guard let data = try? Data(contentsOf:self.trimFileUrl!) else {
                return
            }

            
            print(data.max())
            print(data.min())
            }
            audioPlayer.prepareToPlay()
            audioPlayer.volume = 10.0
        }
    }
    
    func getDocumentsDirectory() -> URL {
        let paths = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)
        return paths[0]
    }
    
    func getFileURL() -> URL {
        let path = getDocumentsDirectory().appendingPathComponent("recording.m4a")
        return path as URL
    }
extension ViewController {
    func cropAudio() -> Void {
        
        var startTime : Float?
        var finalTime : Float?
        
        let url = getFileURL()
        
        asset = AVURLAsset(url: url, options: [AVURLAssetPreferPreciseDurationAndTimingKey : true])
        
        
        let length = Float(asset.duration.value) / Float(asset.duration.timescale)
        print("video length: \(length) seconds")
        
        
        
        let fileManager = FileManager.default
        
        startTime = length - 2
        finalTime = length
        
        let now = NSDate()
        let nowTimeStamp = self.getCurrentTimeStampWOMiliseconds(dateToConvert: now)
        
        var newFileName = "trimAudio" + nowTimeStamp + ".m4a"
        print(newFileName)
        guard let documentDirectory = try? fileManager.url(for: .documentDirectory, in: .userDomainMask, appropriateFor: nil, create: true) else { return }
        
        
        var outputURL = documentDirectory.appendingPathComponent("output")
        do {
            try fileManager.createDirectory(at: outputURL, withIntermediateDirectories: true, attributes: nil)
            outputURL = outputURL.appendingPathComponent(newFileName)
        }catch let error {
            print(error)
        }
        
        
        
        //Remove previous existing file
        //   _ = try? fileManager.removeItem(at: url)
        
        do {
            try FileManager.default.removeItem(at: url)
            print("File deleted")
            //  return true
        }
        catch {
            print("Error")
        }
        
        guard let exportSession = AVAssetExportSession(asset: asset, presetName: AVAssetExportPresetAppleM4A) else {return}
        
        exportSession.outputURL = outputURL
        exportSession.outputFileType = AVFileType.m4a
        
        let start = startTime
        let end = finalTime
        
        let startTimeRange = CMTime(seconds: Double(start ?? 0), preferredTimescale: 1000)
        let endTimeRange = CMTime(seconds: Double(end ?? length), preferredTimescale: 1000)
        let timeRange = CMTimeRange(start: startTimeRange, end: endTimeRange)
        
        exportSession.timeRange = timeRange
        exportSession.exportAsynchronously{
            switch exportSession.status {
            case .completed:
                print("exported at \(outputURL)")
                
                //audio file path
                self.trimFileUrl = outputURL
            case .failed:
                print("failed \(String(describing: exportSession.error))")
            case .cancelled:
                print("cancelled \(String(describing: exportSession.error))")
            default:
                break
            }
        }
    }
}


extension ViewController {
    func getCurrentTimeStampWOMiliseconds(dateToConvert: NSDate) -> String {
        let objDateformat: DateFormatter = DateFormatter()
        objDateformat.dateFormat = "yyyy-MM-dd HH:mm:ss"
        let strTime: String = objDateformat.string(from: dateToConvert as Date)
        let objUTCDate: NSDate = objDateformat.date(from: strTime)! as NSDate
        let milliseconds: Int64 = Int64(objUTCDate.timeIntervalSince1970)
        let strTimeStamp: String = "\(milliseconds)"
        return strTimeStamp
    }
}

